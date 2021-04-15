char	*ft_isspace(char *str)
{
	while (*str != '\0' && (*str == ' ' || *str == '\f' || *str == '\n' ||
				*str == '\r' || *str == '\t' || *str == '\v'))
		str++;
	return (str);
}

int		ft_atoi(char *str)
{
	int sign;
	int nbr;

	sign = 1;
	nbr = 0;
	str = ft_isspace(str);
	while (*str == '-' || *str == '+')
	{
		if (*str == '-')
			sign *= -1;
		else if (*str == '+')
			sign *= 1;
		str++;
	}
	while (*str >= '0' && *str <= '9')
	{
		nbr = (nbr * 10) + (*str - 48);
		str++;
	}
	return (nbr * sign);
}

#include <stdio.h>
int	main(void)
{
	printf("%d\n", ft_atoi("      -+-+--+----++-199a7"));
	return (0);
}
