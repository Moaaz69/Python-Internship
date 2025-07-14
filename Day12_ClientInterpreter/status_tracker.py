def create_feature_status_dict(features):
    # All features start as "Pending"
    return {feature: "Pending" for feature in features}