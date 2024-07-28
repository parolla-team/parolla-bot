Domain will contains DTO and entities. We need to define clearly the domain of the app.



Example:
1. cart_coupons
- __init__.py
- [dto.py](https://github.com/v-v-d/carts/blob/625a5e5068885934acd3b10814b21e2ea0a45be1/src/app/domain/cart_coupons/dto.py)
- [entities.py](https://github.com/v-v-d/carts/blob/625a5e5068885934acd3b10814b21e2ea0a45be1/src/app/domain/cart_coupons/entities.py)
- [exceptions.py](https://github.com/v-v-d/carts/blob/625a5e5068885934acd3b10814b21e2ea0a45be1/src/app/domain/cart_coupons/exceptions.py)
- [value_objects.py](https://github.com/v-v-d/carts/blob/625a5e5068885934acd3b10814b21e2ea0a45be1/src/app/domain/cart_coupons/value_objects.py)


The domain will be used by the repositories to compute and output the correct type.
For example the database must return a entitie class that is define in the Domaine, it must use the dto to compute it using pydantic (validate the item).

We won't need to have interfaces for the repositories. but maybe to allow evolution ?
Since I dont't think we move from postgres db I don't see the need to have another abstraction class here.
