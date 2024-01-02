from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from django_pandas.io import read_frame
from openpyxl import Workbook

from . import models
from . import forms


@login_required
def checkout_show(request):
    q = models.CheckOutModel.objects.all()
    content = {"title": "Kasa", "result": q}
    query_param = request.GET.get("id_", None)
    delete_param = request.GET.get("delete", None)

    if query_param and not delete_param:
        check_q = get_object_or_404(models.CheckOutModel, id=query_param)
        form = forms.CheckOutForm(request.POST or None, instance=check_q or None)
        content["form"] = form
        if request.method == "POST":
            r = request.GET.copy()
            if form.is_valid():
                form.save()
                try:
                    del r["id_"]
                    del r["delete"]
                except:
                    pass
                return redirect("income_expense:checkout_show")
            else:
                messages.error(request, "Error when try to edit form")

    if query_param and delete_param:
        r = request.GET.copy()
        check_q = get_object_or_404(models.CheckOutModel, id=query_param)
        check_q.delete()
        try:
            del r["id_"]
            del r["delete"]
        except:
            pass
        messages.success(request, "Successfully deleted id {}".format(query_param))
        return redirect("income_expense:checkout_show")
    return render(request, "income_excome/checkout.html", content)


@login_required
def checkout_new(request):
    form = forms.CheckOutForm(request.POST or None)
    if request.method == "GET":
        q = models.CheckOutModel.objects.all()
        content = {
            "title": "Kasa",
            "result": q,
            "form": form,
        }
        return render(request, "income_excome/checkout.html", content)
    elif request.method == "POST":
        if form.is_valid():
            f = form.save(commit=False)
            if f.name.lower() not in [
                m.name.lower() for m in models.CheckOutModel.objects.all()
            ]:
                f.save()
                return redirect("income_expense:checkout_show")

        messages.error(request, "Error, name may be not unique?")
        return redirect("income_expense:checkout_new")


@login_required
def types_show(request):
    # income_expense:types_show
    cust_type = request.GET.get("type")
    new_record = request.GET.get("new_record")
    edit_ask = request.GET.get("edit")
    delete_ask = request.GET.get("delete")

    if not cust_type:
        all_types = models.Types.objects.all()
    else:
        all_types = models.Types.only_type.only_with_filter(cust_type)

    content = {
        "title": "Types",
        "types": all_types,
        "vid_types": models.TypesVid,
    }

    if new_record:
        form = forms.TypeForm(request.POST or None)
        content["form"] = form

    if edit_ask:
        type_id = get_object_or_404(models.Types, id=edit_ask)
        form = forms.TypeForm(request.POST or None, instance=type_id)
        content["form"] = form

    if delete_ask:
        r = request.GET.copy()
        type_for_delete = get_object_or_404(models.Types, id=delete_ask)
        type_for_delete.delete()
        try:
            del r["delete"]
        except:
            pass
        messages.success(request, "Successfully delete record")
        return redirect("income_expense:types_show")

    if request.method == "POST":
        r = request.GET.copy()
        if form.is_valid():
            form.save()
            try:
                del r["cust_type"]
                del r["new_record"]
            except:
                pass
            messages.success(request, "Successfully create new record")
        return redirect("income_expense:types_show")

    return render(request, "income_excome/types.html", content)


@login_required
def action_show(request):
    actions = models.NewActionModel.objects.all()
    content = {"actions": actions, "title": "Action's"}
    return render(request, "income_excome/show_actions.html", content)


def action_new(request):
    form = forms.NewActionForm(request.POST or None)
    content = {"title": "NewAction", "form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("income_expense:action_show")
    return render(request, "income_excome/new_action.html", content)


def action_edit(request, id_):
    pass


def action_delete(request, id_):
    pass


@login_required
def result_in_excell(request):
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = 'attachment; filename="actions.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "Result"
    actions = models.NewActionModel.objects.all()
    for a in actions:
        to_user = a.to_user
        if to_user:
            to_user = to_user.name
        else:
            to_user = ""
        ws.append(
            [
                a.from_user.name,
                to_user,
                a.type_action.name,
                a.suma,
                a.description,
                str(a.date_created),
            ]
        )

    wb.save(response)
    return response
