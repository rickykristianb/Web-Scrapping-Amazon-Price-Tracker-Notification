import amazondata
import emailnotification


def main():
    price_expected = float(input("Insert price alert you expect: $"))

    data = amazondata.AmazonData()
    name = data.get_product_name()
    price = float(data.get_price())
    print(price_expected, price)
    if price_expected < price:
        notification = emailnotification.Notification(product_name=name, product_price=price, product_url=data.URL)
        notification.send_notification()


if __name__ == "__main__":
    main()
