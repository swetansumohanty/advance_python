from pprint import pprint
from datetime import datetime
from calendar import monthrange
import logging
from typing import List, Dict
from collections import defaultdict

# loggin config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)

data = [
    {
        "idx": 1,
        "item_code": "Executive Desk (4*2)",
        "sales_description": "Dedicated Executive Desk",
        "qty": 10,
        "rate": "1000",
        "amount": "10000",
        "start_date": "2023-11-01",
        "stop_date": "2024-10-17",
    },
    {
        "idx": 2,
        "item_code": "Executive Desk (4*2)",
        "qty": "10",
        "rate": "1080",
        "amount": "10800",
        "start_date": "2024-10-18",
        "stop_date": "2025-10-31",
    },
    {
        "idx": 3,
        "item_code": "Executive Desk (4*2)",
        "qty": 15,
        "rate": "1080",
        "amount": "16200",
        "start_date": "2024-11-01",
        "stop_date": "2025-10-31",
    },
    {
        "idx": 4,
        "item_code": "Executive Desk (4*2)",
        "qty": 5,
        "rate": "1000",
        "amount": "5000",
        "start_date": "2024-11-01",
        "stop_date": "2025-10-31",
    },
    {
        "idx": 5,
        "item_code": "Manager Cabin",
        "qty": 5,
        "rate": 5000,
        "amount": 25000,
        "start_date": "2024-11-01",
        "stop_date": "2025-10-31",
    },
    {
        "idx": 6,
        "item_code": "Manager Cabin",
        "qty": 7,
        "rate": "5000",
        "amount": 35000,
        "start_date": "2024-12-15",
        "stop_date": "2025-10-31",
    },
    {
        "idx": 7,
        "item_code": "Manager Cabin",
        "qty": 10,
        "rate": 4600,
        "amount": 46000,
        "start_date": "2023-11-01",
        "stop_date": "2024-10-17",
    },
    {
        "idx": 8,
        "item_code": "Parking (2S)",
        "qty": 10,
        "rate": 1000,
        "amount": 10000,
        "start_date": "2024-11-01",
        "stop_date": "2025-10-31",
    },
    {
        "idx": 9,
        "item_code": "Parking (2S)",
        "qty": 10,
        "rate": 0,
        "amount": 0,
        "start_date": "2024-11-01",
        "stop_date": "2025-10-31",
    },
    {
        "idx": 10,
        "item_code": "Executive Desk (4*2)",
        "qty": "8",
        "rate": "1100",
        "amount": "8800",
        "start_date": "2024-11-15",
        "stop_date": "2025-01-31",
    },
    {
        "idx": 11,
        "item_code": "Manager Cabin",
        "qty": "3",
        "rate": "5200",
        "amount": "15600",
        "start_date": "2024-10-10",
        "stop_date": "2024-11-10",
    },
    {
        "idx": 12,
        "item_code": "Conference Table",
        "qty": 1,
        "rate": "20000",
        "amount": "20000",
        "start_date": "2024-11-05",
        "stop_date": "2024-11-20",
    },
    {
        "idx": 13,
        "item_code": "Parking (2S)",
        "qty": 5,
        "rate": "1000",
        "amount": "5000",
        "start_date": "2024-11-15",
        "stop_date": "2025-02-28",
    },
    {
        "idx": 14,
        "item_code": "Reception Desk",
        "qty": 2,
        "rate": "7000",
        "amount": "14000",
        "start_date": "2024-11-01",
        "stop_date": "2025-03-31",
    },
    {
        "idx": 15,
        "item_code": "Reception Desk",
        "qty": 1,
        "rate": "7000",
        "amount": "7000",
        "start_date": "2024-11-10",
        "stop_date": "2024-11-25",
    },
    {
        "idx": 16,
        "item_code": "Breakout Area",
        "qty": 3,
        "rate": "3000",
        "amount": "9000",
        "start_date": "2024-01-01",
        "stop_date": "2024-01-31",
    },
]


def get_month_start_end(target_month: str):
    """get month start, end and and days in a month"""
    year, month = map(int, target_month.split("-"))
    start = datetime(year, month, 1)
    end = datetime(year, month, monthrange(year, month)[1])
    return start, end, monthrange(year, month)[1]


def filter_active_items(item_list: list, target_month: str) -> List[dict]:
    """filter acitve items within the target month range and billing"""

    logging.info("start filtering items")
    active_items = []

    # get year & month
    month_start, month_end, days_in_month = get_month_start_end(target_month)

    for item in item_list:

        start_date = datetime.strptime(item.get("start_date"), "%Y-%m-%d")
        stop_date = datetime.strptime(item.get("stop_date"), "%Y-%m-%d")

        # Check if item date range intersects with selected month
        if start_date <= month_end and stop_date >= month_start:

            # billing intersecion
            billing_start = max(start_date, month_start)
            billing_end = min(stop_date, month_end)

            active_days = (billing_end - billing_start).days + 1
            factor = active_days / days_in_month
            full_amount = float(item.get("amount"))

            item["billing_start"] = billing_start
            item["billing_end"] = billing_end
            item["billing_period"] = f"{billing_start} to {billing_end}"

            item["active_days"] = active_days
            item["days_in_month"] = days_in_month
            item["amount"] = round(full_amount * factor, 2)
            active_items.append(item)

    logging.info("items filtered successfully")
    return active_items


def group_items(items: List[Dict]) -> List[Dict]:
    """
    Group items based on:
    - item_code
    - rate
    - billing_start
    - billing_end
    """
    logging.info("start gouping items")
    grouped = defaultdict(lambda: {"qty": 0, "amount": 0, "items": []})

    for item in items:
        key = (
            item["item_code"],
            str(item["rate"]),
            item["billing_start"],
            item["billing_end"],
        )
        grouped[key]["qty"] += int(item["qty"])
        grouped[key]["amount"] += float(item["amount"])
        grouped[key]["items"].append(item)

    # Format the grouped result
    result = []
    for (item_code, rate, billing_start, billing_end), data in grouped.items():
        result.append(
            {
                "item_code": item_code,
                "rate": rate,
                "billing_start": billing_start,
                "billing_end": billing_end,
                "total_qty": data["qty"],
                "total_amount": data["amount"],
                "items": data["items"],
            }
        )

    logging.info("item grouped successfully")
    return result


def calculate_total_revenue(grouped_data: List[Dict]) -> float:
    logging.info("calculated total revenue")
    return round(sum(group["total_amount"] for group in grouped_data), 2)


def generate_monthly_bill(item_list: list, target_month: str) -> dict:
    """
    Generates a bill for the given month based on the item list.

    Parameters:
        item_list (list): List of dictionaries with item details.
        target_month (str): Month in "YYYY-MM" format (e.g., "2024-11").

    Returns:
        dict: A dictionary with grouped line items and total revenue.
    """

    # filter active items
    items_active = filter_active_items(item_list=item_list, target_month=target_month)
    # pprint(items_active)

    # group items by fileds
    group_data = group_items(items=items_active)
    # pprint(group_data)

    # calcualte total revenue
    total_revenue = calculate_total_revenue(group_data)

    # formatting the result
    result = {"line_item": group_data, "total_revenue": total_revenue}

    return result


if __name__ == "__main__":
    response = generate_monthly_bill(data, "2024-11")
    pprint(response)
