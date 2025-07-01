from odoo import http


class TestApi(http.Controller):
    @http.route(route="/api/test", type="http", auth="none", csrf=False, methods=["GET"])
    def test_api(self):
        return "Test API called"
       