import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# 🔐 SECRETS
# =========================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CRYPTO_PAY_TOKEN = os.getenv("CRYPTO_PAY_TOKEN")
TON_WALLET_ADDRESS = os.getenv("TON_WALLET_ADDRESS")


# =========================
# 👑 ADMIN
# =========================

ADMIN_IDS = [
    7861322479,
]


# =========================
# 🎨 SHOP
# =========================

SHOP_NAME = "AURORA EXCHANGE"

START_TITLE = "⚡ AURORA USDT"

START_TEXT = (
    "Быстрая покупка цифровых активов.\n\n"
    "Выберите нужное действие ниже:"
)

START_IMAGE = "assets/start.jpg"


# =========================
# 💰 PRODUCTS
# =========================

PRODUCTS = {
    100: 1,
    500: 5,
    1000: 10,
    5000: 50,
    10000: 100,
}


# =========================
# 💳 PAYMENT METHODS
# =========================

ENABLE_CRYPTOPAY = True
ENABLE_TON = True
ENABLE_MANUAL = True


# =========================
# 💬 SUPPORT
# =========================

SUPPORT_USERNAME = "@lovetosteal"


# =========================
# 📦 ORDERS
# =========================

ORDER_EXPIRE_MINUTES = 10


# =========================
# 🗄 DATABASE
# =========================

DATABASE_PATH = "data/shop.db"