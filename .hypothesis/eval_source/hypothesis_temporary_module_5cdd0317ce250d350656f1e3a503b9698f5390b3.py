from hypothesis.utils.conventions import not_set

def accept(f):
    def test_next_notification_same_as_base_subscription(self, related_subscription=not_set):
        return f(self=self, related_subscription=related_subscription)
    return test_next_notification_same_as_base_subscription
