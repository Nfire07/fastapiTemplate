from fastapi import APIRouter
from ..database import get_connection

router = APIRouter()

@router.get("/users")
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SHOW TABLES")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users
