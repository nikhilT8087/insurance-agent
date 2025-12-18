from app.db.db_config import customers, policies

def verify_customer(value: str):
    customer = customers.find_one({"mobile": value})
    if customer:
        return {
            "customer_id": customer["customer_id"],
            "policy_id": None
        }

    policy = policies.find_one({"policy_number": value})
    if policy:
        return {
            "customer_id": policy["customer_id"],
            "policy_id": policy["policy_id"]
        }

    return None