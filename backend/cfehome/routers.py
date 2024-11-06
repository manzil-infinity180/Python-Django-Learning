from  rest_framework.routers import DefaultRouter
from products.viewset import ProductSetView

router = DefaultRouter()
router.register('products', ProductSetView, basename='products')

urlpatterns = router.urls
