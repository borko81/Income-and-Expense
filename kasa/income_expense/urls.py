from django.urls import path

from . import views as income_expense_views


app_name = "income_expense"
urlpatterns = [
    path("checkout_show/", income_expense_views.checkout_show, name="checkout_show"),
    path(
        "result_in_excell/",
        income_expense_views.result_in_excell,
        name="result_in_excell",
    ),
    path("checkout_new/", income_expense_views.checkout_new, name="checkout_new"),
    path("types_show/", income_expense_views.types_show, name="types_show"),
    path("action_show/", income_expense_views.action_show, name="action_show"),
    path("action_new/", income_expense_views.action_new, name="action_new"),
    path(
        "action_edit/<int:id_>/",
        income_expense_views.action_edit,
        name="action_edit",
    ),
    path(
        "action_delete/<int:id_>/",
        income_expense_views.action_delete,
        name="action_delete",
    ),
]
