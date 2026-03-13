from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: None, hall_number: None,
                 cleaner: None, movie: None) -> bool:
    customer_list = []

    for cla in customers:
        customer = Customer(cla["name"], cla["food"])
        customer_list.append(customer)

        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(movie, customer_list, cleaner_obj)
