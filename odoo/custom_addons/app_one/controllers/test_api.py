from odoo import http


class TestApi(http.Controller):
    @http.route(route="/api/test", type="json", auth="none", methods=["GET"])