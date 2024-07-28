from app.use_cases.interface import BaseHandler, Request


class EvaluateStudentProfileHandler(BaseHandler):
    def __init__(
        self,
        next_handler: BaseHandler | None = None,
    ) -> None:
        super().__init__(next_handler)
        # self.db_client = db_client

    def handle(self, request: Request) -> Request | None:
        """
        Handle the request by evaluating the student profile if it doesn't exist.
        If the profile exists, pass the request to the next handler.

        Args:
            request (Request): The incoming request.

        Returns:
            Request | None: The modified request or None if the request is handled by the next handler.
        """
        return super().handle(request)

    #     if not self.db_client.has_profile(request.user_id):
    #         self.evaluate_student_profile(request)
    #     else:
    #         super().handle(request)

    # def evaluate_student_profile(self, request):
    #     # Logic for evaluating student profile
    #     pass
