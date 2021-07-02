class VectorSpaceService:
    def __init__(self):
        pass


class InnerSpaceService:
    def __init__(self, vector_space_service: VectorSpaceService):
        self.vector_space_service = vector_space_service


class OuterSpaceService:
    def __init__(self):
        pass


class GeometricAlgebraService:
    def __init__(self,
                 inner_space_service: InnerSpaceService,
                 outer_space_service: OuterSpaceService,
                 ):
        self.inner_space_service = inner_space_service
        self.outer_space_service = outer_space_service


class AlgebraOfPhysicalSpace:
    def __init__(self,
                 geometric_product_space_service: GeometricAlgebraService,
                 ):
        pass
