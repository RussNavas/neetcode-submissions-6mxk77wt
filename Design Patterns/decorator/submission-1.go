type Coffee interface {
    GetCost() float64
}

type SimpleCoffee struct{}

func NewSimpleCoffee() *SimpleCoffee {
    return &SimpleCoffee{}
}

func (c *SimpleCoffee) GetCost() float64 {
    return 1.1
}

type MilkDecorator struct {
    // TODO: implement
    coffee Coffee
}

func NewMilkDecorator(coffee Coffee) *MilkDecorator {
    // TODO: implement
    return &MilkDecorator{
        coffee: coffee,
    }
}

func (d *MilkDecorator) GetCost() float64 {
    // TODO: implement
    return d.coffee.GetCost() + 0.5
}

type SugarDecorator struct {
    // TODO: implement
    coffee Coffee
}

func NewSugarDecorator(coffee Coffee) *SugarDecorator {
    // TODO: implement
    return &SugarDecorator{
        coffee: coffee,
    }
}

func (d *SugarDecorator) GetCost() float64 {
    // TODO: implement
    return d.coffee.GetCost() + 0.2
}

type CreamDecorator struct {
    // TODO: implement
    coffee Coffee
}

func NewCreamDecorator(coffee Coffee) *CreamDecorator {
    // TODO: implement
    return &CreamDecorator{
        coffee: coffee,
    }
}

func (d *CreamDecorator) GetCost() float64 {
    // TODO: implement
    return d.coffee.GetCost() + 0.7
}
