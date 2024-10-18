from flask import Blueprint

# Inisialisasi blueprint (chaining)
auth_bp = Blueprint('auth', __name__, template_folder='templates')


# # import routes chaining
from . import routes