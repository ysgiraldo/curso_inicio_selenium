from unittest import TestLoader, TestSuite
# from pyunitreport import HTMLTestRunner #para generar el reporte
from HtmlTestRunner import HTMLTestRunner # Para generar los reportes en conjunto
from assertions import AssertionsTest
from search_tests_assertions import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

#contruimos la suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])

#para generar los reporters
# kwargs = {
#     "output": 'smoke-report'
#     }
kwargs = {
    "output": "reports/smoke-report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": False
}

#la variable runner almacena un reporte generado por HTMLTestRuner
#usa como argumento "kwarsp"
# runner = HTMLTestRunner(**kwargs)
runner = HTMLTestRunner(**kwargs)
# runner.run(smoke_test)

#corro el rurner con la suite de prueba
runner.run(smoke_test) 