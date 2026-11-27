def validate_fields(allowed_fields, fields_to_compare):
    for field in fields_to_compare:
        if field not in allowed_fields:
            raise ValueError
