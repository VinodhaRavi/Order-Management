from dao.order_repo import IOrderManagementRepository
from entity.user import User
from entity.product import Product
from typing import List
from exception.user_not_found_exception import UserNotFoundException
from exception.order_not_found_exception import OrderNotFoundException
from util.db_conn_util import DBUtil

class OrderProcessor(IOrderManagementRepository):

    def __init__(self):
        pass  # DB connection is managed in each method

    def create_user(self, user: User):
        conn = DBUtil.get_db_conn()
        cursor = conn.cursor()
        query = "INSERT INTO User (userId, username, password, role) VALUES (%s, %s, %s, %s)"
        values = (user.get_user_id(), user.get_username(), user.get_password(), user.get_role())

        try:
            cursor.execute(query, values)
            conn.commit()
            print(f" User created successfully: {user}")
        except Exception as e:
            print(f"Error inserting user: {e}")
        finally:
            cursor.close()
            conn.close()

    def create_product(self, user: User, product: Product):
        if user.get_role().lower() != "admin":
            print(" Only admin users can create products.")
            return

        conn = DBUtil.get_db_conn()
        cursor = conn.cursor()
        query = """
            INSERT INTO Product 
            (productId, productName, description, price, quantityInStock, type, brand, warrantyPeriod, size, color)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            product.get_product_id(), product.get_product_name(), product.get_description(),
            product.get_price(), product.get_quantity_in_stock(), product.get_type(),
            getattr(product, "brand", None),
            getattr(product, "warranty_period", None),
            getattr(product, "size", None),
            getattr(product, "color", None)
        )

        try:
            cursor.execute(query, values)
            conn.commit()
            print(" Product inserted successfully.")
        except Exception as e:
            print(" Error inserting product:", e)
        finally:
            cursor.close()
            conn.close()

    def create_order(self, user: User, products: List[Product]):
        conn = DBUtil.get_db_conn()
        cursor = conn.cursor()

        try:
            order_query = "INSERT INTO Orders (userId) VALUES (%s)"
            cursor.execute(order_query, (user.get_user_id(),))
            order_id = cursor.lastrowid

            item_query = "INSERT INTO OrderItems (orderId, productId) VALUES (%s, %s)"
            for product in products:
                cursor.execute(item_query, (order_id, product.get_product_id()))

            conn.commit()
            print(f"Order created for user {user.get_username()} with Order ID: {order_id}")
        except Exception as e:
            print(" Error creating order:", e)
        finally:
            cursor.close()
            conn.close()

    def cancel_order(self, user_id: int, order_id: int):
        conn = DBUtil.get_db_conn()
        cursor = conn.cursor()

        try:
            check_query = "SELECT * FROM Orders WHERE orderId = %s AND userId = %s"
            cursor.execute(check_query, (order_id, user_id))
            if cursor.fetchone() is None:
                raise OrderNotFoundException(f"Order {order_id} for user {user_id} not found.")

            cursor.execute("DELETE FROM OrderItems WHERE orderId = %s", (order_id,))
            cursor.execute("DELETE FROM Orders WHERE orderId = %s", (order_id,))
            conn.commit()
            print(f"Order {order_id} cancelled successfully.")
        except Exception as e:
            print(" Error cancelling order:", e)
        finally:
            cursor.close()
            conn.close()

    def get_all_products(self) -> List[Product]:
        conn = DBUtil.get_db_conn()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM Product")
            products = cursor.fetchall()
            for prod in products:
                print(prod)
            return products
        except Exception as e:
            print("Error fetching products:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    def get_order_by_user(self, user: User):
        conn = DBUtil.get_db_conn()
        cursor = conn.cursor()

        try:
            query = """
                SELECT o.orderId, p.productId, p.productName, p.description, p.price, p.type
                FROM Orders o
                JOIN OrderItems oi ON o.orderId = oi.orderId
                JOIN Product p ON oi.productId = p.productId
                WHERE o.userId = %s
            """
            cursor.execute(query, (user.get_user_id(),))
            orders = cursor.fetchall()
            for item in orders:
                print(item)
            return orders
        except Exception as e:
            print(" Error fetching orders for user:", e)
            return []
        finally:
            cursor.close()
            conn.close()
