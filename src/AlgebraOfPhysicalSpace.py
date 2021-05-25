class VectorSpaceService:
    def __init__(self):
        pass

class InnerProductService:
    def __init__(self, vector_space_service: VectorSpaceService):
        self.vector_space_service = vector_space_service

class OuterProductService:
    def __init__(self):
        pass

class GeometricProductService:
    def __init__(self,
        inner_product_space_service: InnerProductService,
        outer_product_space_service: OuterProductService,
    ):
        self.inner_product_space_service = inner_product_space_service
        self.outer_product_space_service = outer_product_space_service

class AlgebraOfPhysicalSpace:
    def __init__(self,
        geometric_product_space_service: GeometricProductService,
    ):
        pass
