from behave import given,when,then
import time

@given(u'Acesso a pagina')
def step_impl(context):
    context.app.pagina('https://www.google.com.br/')
    time.sleep(5)
    

@when(u'Faco uma pesquisa')
def step_impl(context):
    context.app.escreve('lst-ib','indra brasil','id').submit()
    time.sleep(5)


@then(u'Obtenho o resultado da pesquisa')
def step_impl(context):
    pass