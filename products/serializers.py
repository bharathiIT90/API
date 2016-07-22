from rest_framework import serializers

from .models import Category, Product, Variation 

class VariationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Variation
		fields = [
			"title",
			"price",
		]

class ProductSerializer(serializers.ModelSerializer):
	variation_set = VariationSerializer(many=True,read_only = True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			"id",
			"title",
			"image",
			"variation_set",
		]

	def get_image(self,obj):
		return obj.productimage_set.first().image.url


class CategorySerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name = 'category_detail_api')
	product_set = ProductSerializer(many=True)
	class Meta:
		model = Category
		fields = [
			"url",
			"id",
			"title",
			"description",
			"product_set",
			#"default_category",
		]

