def library_activity_last_seven_months(months_with_year, loans):
    library_activity = {}

    for month in months_with_year:
        month_name = month["month"]["name"]
        month_id = month["month"]["id"]
        year = month["year"]

        loans_per_month_actives = loans.filter(
            request_date__year=year,
            request_date__month=month_id,
            status="active",
        ).count()
        loans_per_month_overdue = loans.filter(
            request_date__year=year,
            request_date__month=month_id,
            status="overdue",
        ).count()
        loans_per_month_returned = loans.filter(
            request_date__year=year,
            request_date__month=month_id,
            status="returned",
        ).count()
        loans_per_month_total = loans.filter(
            request_date__year=year,
            request_date__month=month_id,
        ).count()

        if month_name in library_activity:
            library_activity[month_name]["active"] = loans_per_month_actives
            library_activity[month_name]["overdue"] = loans_per_month_overdue
            library_activity[month_name]["returned"] = loans_per_month_returned
            library_activity[month_name]["total"] = loans_per_month_total
        else:
            library_activity[month_name] = {
                "active": loans_per_month_actives,
                "overdue": loans_per_month_overdue,
                "returned": loans_per_month_returned,
                "total": loans_per_month_total,
            }

    return library_activity
