# Using @api_view decorator with function-based views (FBVs)

# from rest_framework.decorators import api_view
# from rest_framework import status
# from .models import Product
# from .serializers import ProductSerializer
# from django.shortcuts import get_object_or_404
# # from django.http import JsonResponse
# from rest_framework.response import Response

# @api_view(['GET'])
# def list_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response({
#             'message': 'Product List.',
#             'product': serializer.data,
#             'count': len(serializer.data),
#         }, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def create_product(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({
#             'message': 'Product created successfully.',
#             'product': serializer.data
#         }, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def retrieve_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)
#     return Response({
#         'message': 'Product Details.',
#         'product': serializer.data
#     }, status=status.HTTP_200_OK)

# @api_view(['PUT'])
# def update_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({
#             'message': 'Product Updated successfully.',
#             'product': serializer.data
#         }, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delete_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     product.delete()
#     return Response({'message': 'Product deleted successfully.'}, status=204)


from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
