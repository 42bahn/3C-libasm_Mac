# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bahn <bahn@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/05 15:29:22 by bahn              #+#    #+#              #
#    Updated: 2021/04/07 13:57:06 by bahn             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME		= libasm.a

AR		= ar rc

CC		= gcc
NASM		= nasm

RM		= rm -rf

CFLAG		= -Wall -Werror -Wextra
AFLAG		= -f macho64

INC_DIR		= includes/
SRC_DIR		= srcs/
OBJ_DIR		= ./

INC_FILES	= libasm.h
SRC_FILES	= ft_write.s \
		  ft_read.s \
		  ft_strlen.s \
		  ft_strcmp.s \
		  ft_strcpy.s \
		  ft_strdup.s

INC		= $(addprefix $(INC_DIR), $(INC_FILES))
SRCS		= $(addprefix $(SRC_DIR), $(SRC_FILES))
OBJS		= $(SRCS:.s=.o)

all		: $(NAME)

$(NAME)		: $(OBJS)
		$(AR) $(NAME) $(OBJS)
		ranlib $(NAME)

.s.o		: $(SRCS)
		$(NASM) -I$(INC) $(AFLAG) $< -o $@
	
clean		: 
		$(RM) $(OBJS)

fclean		: clean
		$(RM) $(NAME)

re		: fclean all

.PHONY		: all, clean, fclean, re, bonus
		



	  
	 
