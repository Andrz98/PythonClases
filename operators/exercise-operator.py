"""
access_control.py
Exercise: Combine logical operators with function calls and list handling.

Objective:
    Display restricted sections only to users who satisfy:
      1. Have role "admin" OR are in the authorized editors list.
      2. Are NOT in the blocked users list.
      3. Last login was less than 30 days ago.

This script simulates data from an SQL database and shows how to combine logical
operators, function calls, and list membership checks in Python.
"""

# Simulated data (would come from SQL queries in a real app)
rol_usuario = "admin"  # Role of the current user
authorized_editors = ["ana", "luis", "maría"]  # List of usernames allowed as editors
blocked_users = ["pepe", "julia"]  # List of usernames that are blocked


def days_since_last_login(user) -> int:
    """
    Simulates querying a database for the number of days since the user's last login.

    Args:
        user (str): Username to check.

    Returns:
        int: Number of days since last login. Returns 999 if user not found.
    """
    history = {
        "ana":    10,
        "luis":   45,
        "maría":  25,
        "javier":  5,
        "pepe":    3,
        "julia":   4
    }
    # Use .get() to return a large number if the user is not in the history dict
    return history.get(user, 999)


# The username we're evaluating
current_user = "luis"

# 1. Role or explicit permission check
#    True if the user is an admin OR is listed as an authorized editor
tiene_permiso_rol = (rol_usuario == "admin") or (current_user in authorized_editors)

# 2. Security check: ensure the user is not blocked
#    True if current_user does NOT appear in blocked_users
no_bloqueado = current_user not in blocked_users

# 3. Recent connection check
#    True if the user's last login was less than 30 days ago
conexion_reciente = days_since_last_login(current_user) < 30


# 4. Final expression: combine all three checks
#    The user gets access only if all checks are True
acceso_secciones = tiene_permiso_rol and no_bloqueado and conexion_reciente

# 5. Output the result
if acceso_secciones:
  print("Acceso permitido")
else:
  print("Acceso denegado")

