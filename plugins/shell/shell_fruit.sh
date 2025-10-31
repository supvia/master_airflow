FRUIT=$1
if [ $FRUIT == APPLE ];then
    echo "You selected an apple!"
elif [ $FRUIT == ORANGE ];then
    echo "You selected Orange!"
elif [ $FRUIT == GRADE ];then
    echo "You selected Grape!"
else
    echo "You selected an unknown fruit!"
fi
