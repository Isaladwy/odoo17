from odoo import http


class TestApi(http.Controller):
    @http.route(route="/api/test", type="http", auth="none", csrf=False, methods=["GET"])
    def test_api(self):
        print("Test API called")
        return http.Response(
            status=200,
            content_type="application/json",
            response='{"message": "Test API response"}',
        )