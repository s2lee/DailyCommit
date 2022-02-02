from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class IsAdminUserOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


#  리뷰를 작성한 사람만 리뷰를 업데이트/삭제할 수 있도록 함
# class IsPostAuthorOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # 읽기 권한 요청이 들어오면 허용
#         if request.method in SAFE_METHODS:
#             return True
#
#         return obj.review_author == request.user
