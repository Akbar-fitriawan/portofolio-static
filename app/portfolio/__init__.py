from flask import Blueprint

# Inisialisasi blueprint (chaining)
portfolio_bp = Blueprint('portfolio', __name__, template_folder='templates')

# # import routes chaining
from . import routes