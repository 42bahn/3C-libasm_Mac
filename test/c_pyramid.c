#include <unistd.h>

int	main(int argc, char *argv[])
{
	int	height;
	int	i;
	int	j;

	if (argc == 2)
	{
		height = argv[1][0] - 48;

		i = 0;
		j = 0;
		while (i++ < height)
		{
			j = 0;
			while (j++ < i)
			{
				write(1, "*", 1);
			}
			write (1, "\n", 1);
		}
	}
	return (0);
}
