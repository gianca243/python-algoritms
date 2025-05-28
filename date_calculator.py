from datetime import datetime


def dias360(
    expedition_date: datetime, expiration_date: datetime, ue_mode: bool = False
):
    d1 = expedition_date.day
    d2 = expiration_date.day
    m1 = expedition_date.month
    m2 = expiration_date.month
    y1 = expedition_date.year
    y2 = expiration_date.year

    if ue_mode:
        # Método Europeo: ambos días 31 se consideran como 30
        if d1 == 31:
            d1 = 30
        if d2 == 31:
            d2 = 30
    else:
        # Método EE. UU. (NASD)
        if d1 == 31:
            d1 = 30
        if d2 == 31:
            if d1 < 30:
                d2 = 1
                m2 += 1
                if m2 > 12:
                    m2 = 1
                    y2 += 1
            else:
                d2 = 30

    return 360 * (y2 - y1) + 30 * (m2 - m1) + (d2 - d1)


date_1 = datetime(2025, 5, 24)
date_2 = datetime(2026, 2, 6)

print(dias360(date_1, date_2))
