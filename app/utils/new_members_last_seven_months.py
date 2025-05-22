def new_members_last_seven_months(months_with_year, members):
    new_members = {}

    for month in months_with_year:
        month_name = month["month"]["name"]
        month_id = month["month"]["id"]
        year = month["year"]

        members_in_month = members.filter(
            date_joined__year=year,
            date_joined__month=month_id,
        ).count()

        if month_name in new_members:
            new_members[month_name] += members_in_month
        else:
            new_members[month_name] = members_in_month

    return new_members
