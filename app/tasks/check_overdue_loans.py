from datetime import datetime
from ..models import Loan


def check_overdue_loans():
    current_date = datetime.today()
    overdue_loans = Loan.objects.filter(due_date__lt=current_date, status="active")

    if not overdue_loans.exists():
        print("No overdue loans found.")
        return

    for loan in overdue_loans:
        # Aquí se podría configurar una notificación o un recordatorio por correo al usuario.
        try:
            loan.status = "overdue"
            loan.save()
        except Exception as e:
            print(f"Error updating loan: {e}")
