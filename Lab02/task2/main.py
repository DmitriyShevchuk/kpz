from factories.iprone_factory import IProneFactory
from factories.kiaomi_factory import KiaomiFactory
from factories.balaxy_factory import BalaxyFactory

def main():
    iprone_factory = IProneFactory()
    kiaomi_factory = KiaomiFactory()
    balaxy_factory = BalaxyFactory()

    print("=== IProne Products ===")
    print(iprone_factory.create_laptop().info())
    print(iprone_factory.create_netbook().info())
    print(iprone_factory.create_ebook().info())
    print(iprone_factory.create_smartphone().info())

    print("\n=== Kiaomi Products ===")
    print(kiaomi_factory.create_laptop().info())
    print(kiaomi_factory.create_netbook().info())
    print(kiaomi_factory.create_ebook().info())
    print(kiaomi_factory.create_smartphone().info())

    print("\n=== Balaxy Products ===")
    print(balaxy_factory.create_laptop().info())
    print(balaxy_factory.create_netbook().info())
    print(balaxy_factory.create_ebook().info())
    print(balaxy_factory.create_smartphone().info())

if __name__ == "__main__":
    main()
