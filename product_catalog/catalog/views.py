
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# CustomResponse Handling
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'message': 'Product list retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
        
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Product created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
        
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)  # Handle partial update
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Product updated successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        super().destroy(request, *args, **kwargs)
        return Response({
            'message': f'Product {instance.name} deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            raise NotFound(detail="Product not found")
        serializer = self.get_serializer(instance)
        return Response({
            'message': 'Product retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)





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

