#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

/* MacOS	
size_t	ft_strlen(const char *s);
ssize_t ft_write(int fd, const void *buf, size_t count);
ssize_t ft_read(int fd, const void *buf, size_t count);
char *ft_strcpy(char *dest, const char *src);
int strcmp(const char *s1, const char *s2);
*/

size_t	_ft_strlen(const char *s);
ssize_t _ft_write(int fd, const void *buf, size_t count);
ssize_t _ft_read(int fd, const void *buf, size_t count);
char *_ft_strcpy(char *dest, const char *src);
int _ft_strcmp(const char *s1, const char *s2);
char *_ft_strdup(const char *s);

int	main(void)
{
	printf("%s\n", _ft_strdup("abcde"));
	

/* Linux
	printf("%ld\n", _ft_strlen("abcde"));
	printf("\t(return : %ld)\n", _ft_write(1, "abcde", 5));
	ret = _ft_read(1, buf, 5);
	i = 0;
	while (i < ret)
	{
		if (buf[i] == '\n')
			buf[i] = '\0';
		i++;
	}
	printf("%s\t(return : %ld)\n", buf, ret);
	_ft_strcpy(buf, str);
	printf("%s\n", buf);

*/
	
/* MacOS
	printf("%ld\n", ft_strlen("abcde"));	
	printf("\t(return : %ld)\n", ft_write(1, "abcde", 5));
	ret = ft_read(1, buf, 5);
	i = 0;
	while (i < ret)
	{
		if (buf[i] == '\n')
			buf[i] = '\0';
		i++;
	}
	printf("%s\t(return : %ld)\n", buf, ret);
*/
	
	return (0);
}
