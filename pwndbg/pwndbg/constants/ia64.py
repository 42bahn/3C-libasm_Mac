#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .constant import Constant

__NR_ni_syscall = Constant('__NR_ni_syscall',1024)
__NR_exit = Constant('__NR_exit',1025)
__NR_read = Constant('__NR_read',1026)
__NR_write = Constant('__NR_write',1027)
__NR_open = Constant('__NR_open',1028)
__NR_close = Constant('__NR_close',1029)
__NR_creat = Constant('__NR_creat',1030)
__NR_link = Constant('__NR_link',1031)
__NR_unlink = Constant('__NR_unlink',1032)
__NR_execve = Constant('__NR_execve',1033)
__NR_chdir = Constant('__NR_chdir',1034)
__NR_fchdir = Constant('__NR_fchdir',1035)
__NR_utimes = Constant('__NR_utimes',1036)
__NR_mknod = Constant('__NR_mknod',1037)
__NR_chmod = Constant('__NR_chmod',1038)
__NR_chown = Constant('__NR_chown',1039)
__NR_lseek = Constant('__NR_lseek',1040)
__NR_getpid = Constant('__NR_getpid',1041)
__NR_getppid = Constant('__NR_getppid',1042)
__NR_mount = Constant('__NR_mount',1043)
__NR_umount = Constant('__NR_umount',1044)
__NR_setuid = Constant('__NR_setuid',1045)
__NR_getuid = Constant('__NR_getuid',1046)
__NR_geteuid = Constant('__NR_geteuid',1047)
__NR_ptrace = Constant('__NR_ptrace',1048)
__NR_access = Constant('__NR_access',1049)
__NR_sync = Constant('__NR_sync',1050)
__NR_fsync = Constant('__NR_fsync',1051)
__NR_fdatasync = Constant('__NR_fdatasync',1052)
__NR_kill = Constant('__NR_kill',1053)
__NR_rename = Constant('__NR_rename',1054)
__NR_mkdir = Constant('__NR_mkdir',1055)
__NR_rmdir = Constant('__NR_rmdir',1056)
__NR_dup = Constant('__NR_dup',1057)
__NR_pipe = Constant('__NR_pipe',1058)
__NR_times = Constant('__NR_times',1059)
__NR_brk = Constant('__NR_brk',1060)
__NR_setgid = Constant('__NR_setgid',1061)
__NR_getgid = Constant('__NR_getgid',1062)
__NR_getegid = Constant('__NR_getegid',1063)
__NR_acct = Constant('__NR_acct',1064)
__NR_ioctl = Constant('__NR_ioctl',1065)
__NR_fcntl = Constant('__NR_fcntl',1066)
__NR_umask = Constant('__NR_umask',1067)
__NR_chroot = Constant('__NR_chroot',1068)
__NR_ustat = Constant('__NR_ustat',1069)
__NR_dup2 = Constant('__NR_dup2',1070)
__NR_setreuid = Constant('__NR_setreuid',1071)
__NR_setregid = Constant('__NR_setregid',1072)
__NR_getresuid = Constant('__NR_getresuid',1073)
__NR_setresuid = Constant('__NR_setresuid',1074)
__NR_getresgid = Constant('__NR_getresgid',1075)
__NR_setresgid = Constant('__NR_setresgid',1076)
__NR_getgroups = Constant('__NR_getgroups',1077)
__NR_setgroups = Constant('__NR_setgroups',1078)
__NR_getpgid = Constant('__NR_getpgid',1079)
__NR_setpgid = Constant('__NR_setpgid',1080)
__NR_setsid = Constant('__NR_setsid',1081)
__NR_getsid = Constant('__NR_getsid',1082)
__NR_sethostname = Constant('__NR_sethostname',1083)
__NR_setrlimit = Constant('__NR_setrlimit',1084)
__NR_getrlimit = Constant('__NR_getrlimit',1085)
__NR_getrusage = Constant('__NR_getrusage',1086)
__NR_gettimeofday = Constant('__NR_gettimeofday',1087)
__NR_settimeofday = Constant('__NR_settimeofday',1088)
__NR_select = Constant('__NR_select',1089)
__NR_poll = Constant('__NR_poll',1090)
__NR_symlink = Constant('__NR_symlink',1091)
__NR_readlink = Constant('__NR_readlink',1092)
__NR_uselib = Constant('__NR_uselib',1093)
__NR_swapon = Constant('__NR_swapon',1094)
__NR_swapoff = Constant('__NR_swapoff',1095)
__NR_reboot = Constant('__NR_reboot',1096)
__NR_truncate = Constant('__NR_truncate',1097)
__NR_ftruncate = Constant('__NR_ftruncate',1098)
__NR_fchmod = Constant('__NR_fchmod',1099)
__NR_fchown = Constant('__NR_fchown',1100)
__NR_getpriority = Constant('__NR_getpriority',1101)
__NR_setpriority = Constant('__NR_setpriority',1102)
__NR_statfs = Constant('__NR_statfs',1103)
__NR_fstatfs = Constant('__NR_fstatfs',1104)
__NR_gettid = Constant('__NR_gettid',1105)
__NR_semget = Constant('__NR_semget',1106)
__NR_semop = Constant('__NR_semop',1107)
__NR_semctl = Constant('__NR_semctl',1108)
__NR_msgget = Constant('__NR_msgget',1109)
__NR_msgsnd = Constant('__NR_msgsnd',1110)
__NR_msgrcv = Constant('__NR_msgrcv',1111)
__NR_msgctl = Constant('__NR_msgctl',1112)
__NR_shmget = Constant('__NR_shmget',1113)
__NR_shmat = Constant('__NR_shmat',1114)
__NR_shmdt = Constant('__NR_shmdt',1115)
__NR_shmctl = Constant('__NR_shmctl',1116)
__NR_syslog = Constant('__NR_syslog',1117)
__NR_setitimer = Constant('__NR_setitimer',1118)
__NR_getitimer = Constant('__NR_getitimer',1119)
__NR_vhangup = Constant('__NR_vhangup',1123)
__NR_lchown = Constant('__NR_lchown',1124)
__NR_remap_file_pages = Constant('__NR_remap_file_pages',1125)
__NR_wait4 = Constant('__NR_wait4',1126)
__NR_sysinfo = Constant('__NR_sysinfo',1127)
__NR_clone = Constant('__NR_clone',1128)
__NR_setdomainname = Constant('__NR_setdomainname',1129)
__NR_uname = Constant('__NR_uname',1130)
__NR_adjtimex = Constant('__NR_adjtimex',1131)
__NR_create_module = Constant('__NR_create_module',1132)
__NR_init_module = Constant('__NR_init_module',1133)
__NR_delete_module = Constant('__NR_delete_module',1134)
__NR_get_kernel_syms = Constant('__NR_get_kernel_syms',1135)
__NR_query_module = Constant('__NR_query_module',1136)
__NR_quotactl = Constant('__NR_quotactl',1137)
__NR_bdflush = Constant('__NR_bdflush',1138)
__NR_sysfs = Constant('__NR_sysfs',1139)
__NR_personality = Constant('__NR_personality',1140)
__NR_afs_syscall = Constant('__NR_afs_syscall',1141)
__NR_setfsuid = Constant('__NR_setfsuid',1142)
__NR_setfsgid = Constant('__NR_setfsgid',1143)
__NR_getdents = Constant('__NR_getdents',1144)
__NR_flock = Constant('__NR_flock',1145)
__NR_readv = Constant('__NR_readv',1146)
__NR_writev = Constant('__NR_writev',1147)
__NR_pread = Constant('__NR_pread',1148)
__NR_pwrite = Constant('__NR_pwrite',1149)
__NR__sysctl = Constant('__NR__sysctl',1150)
__NR_mmap = Constant('__NR_mmap',1151)
__NR_munmap = Constant('__NR_munmap',1152)
__NR_mlock = Constant('__NR_mlock',1153)
__NR_mlockall = Constant('__NR_mlockall',1154)
__NR_mprotect = Constant('__NR_mprotect',1155)
__NR_mremap = Constant('__NR_mremap',1156)
__NR_msync = Constant('__NR_msync',1157)
__NR_munlock = Constant('__NR_munlock',1158)
__NR_munlockall = Constant('__NR_munlockall',1159)
__NR_sched_getparam = Constant('__NR_sched_getparam',1160)
__NR_sched_setparam = Constant('__NR_sched_setparam',1161)
__NR_sched_getscheduler = Constant('__NR_sched_getscheduler',1162)
__NR_sched_setscheduler = Constant('__NR_sched_setscheduler',1163)
__NR_sched_yield = Constant('__NR_sched_yield',1164)
__NR_sched_get_priority_max = Constant('__NR_sched_get_priority_max',1165)
__NR_sched_get_priority_min = Constant('__NR_sched_get_priority_min',1166)
__NR_sched_rr_get_interval = Constant('__NR_sched_rr_get_interval',1167)
__NR_nanosleep = Constant('__NR_nanosleep',1168)
__NR_nfsservctl = Constant('__NR_nfsservctl',1169)
__NR_prctl = Constant('__NR_prctl',1170)
__NR_mmap2 = Constant('__NR_mmap2',1172)
__NR_pciconfig_read = Constant('__NR_pciconfig_read',1173)
__NR_pciconfig_write = Constant('__NR_pciconfig_write',1174)
__NR_perfmonctl = Constant('__NR_perfmonctl',1175)
__NR_sigaltstack = Constant('__NR_sigaltstack',1176)
__NR_rt_sigaction = Constant('__NR_rt_sigaction',1177)
__NR_rt_sigpending = Constant('__NR_rt_sigpending',1178)
__NR_rt_sigprocmask = Constant('__NR_rt_sigprocmask',1179)
__NR_rt_sigqueueinfo = Constant('__NR_rt_sigqueueinfo',1180)
__NR_rt_sigreturn = Constant('__NR_rt_sigreturn',1181)
__NR_rt_sigsuspend = Constant('__NR_rt_sigsuspend',1182)
__NR_rt_sigtimedwait = Constant('__NR_rt_sigtimedwait',1183)
__NR_getcwd = Constant('__NR_getcwd',1184)
__NR_capget = Constant('__NR_capget',1185)
__NR_capset = Constant('__NR_capset',1186)
__NR_sendfile = Constant('__NR_sendfile',1187)
__NR_getpmsg = Constant('__NR_getpmsg',1188)
__NR_putpmsg = Constant('__NR_putpmsg',1189)
__NR_socket = Constant('__NR_socket',1190)
__NR_bind = Constant('__NR_bind',1191)
__NR_connect = Constant('__NR_connect',1192)
__NR_listen = Constant('__NR_listen',1193)
__NR_accept = Constant('__NR_accept',1194)
__NR_getsockname = Constant('__NR_getsockname',1195)
__NR_getpeername = Constant('__NR_getpeername',1196)
__NR_socketpair = Constant('__NR_socketpair',1197)
__NR_send = Constant('__NR_send',1198)
__NR_sendto = Constant('__NR_sendto',1199)
__NR_recv = Constant('__NR_recv',1200)
__NR_recvfrom = Constant('__NR_recvfrom',1201)
__NR_shutdown = Constant('__NR_shutdown',1202)
__NR_setsockopt = Constant('__NR_setsockopt',1203)
__NR_getsockopt = Constant('__NR_getsockopt',1204)
__NR_sendmsg = Constant('__NR_sendmsg',1205)
__NR_recvmsg = Constant('__NR_recvmsg',1206)
__NR_pivot_root = Constant('__NR_pivot_root',1207)
__NR_mincore = Constant('__NR_mincore',1208)
__NR_madvise = Constant('__NR_madvise',1209)
__NR_stat = Constant('__NR_stat',1210)
__NR_lstat = Constant('__NR_lstat',1211)
__NR_fstat = Constant('__NR_fstat',1212)
__NR_clone2 = Constant('__NR_clone2',1213)
__NR_getdents64 = Constant('__NR_getdents64',1214)
__NR_getunwind = Constant('__NR_getunwind',1215)
__NR_readahead = Constant('__NR_readahead',1216)
__NR_setxattr = Constant('__NR_setxattr',1217)
__NR_lsetxattr = Constant('__NR_lsetxattr',1218)
__NR_fsetxattr = Constant('__NR_fsetxattr',1219)
__NR_getxattr = Constant('__NR_getxattr',1220)
__NR_lgetxattr = Constant('__NR_lgetxattr',1221)
__NR_fgetxattr = Constant('__NR_fgetxattr',1222)
__NR_listxattr = Constant('__NR_listxattr',1223)
__NR_llistxattr = Constant('__NR_llistxattr',1224)
__NR_flistxattr = Constant('__NR_flistxattr',1225)
__NR_removexattr = Constant('__NR_removexattr',1226)
__NR_lremovexattr = Constant('__NR_lremovexattr',1227)
__NR_fremovexattr = Constant('__NR_fremovexattr',1228)
__NR_tkill = Constant('__NR_tkill',1229)
__NR_futex = Constant('__NR_futex',1230)
__NR_sched_setaffinity = Constant('__NR_sched_setaffinity',1231)
__NR_sched_getaffinity = Constant('__NR_sched_getaffinity',1232)
__NR_set_tid_address = Constant('__NR_set_tid_address',1233)
__NR_fadvise64 = Constant('__NR_fadvise64',1234)
__NR_tgkill = Constant('__NR_tgkill',1235)
__NR_exit_group = Constant('__NR_exit_group',1236)
__NR_lookup_dcookie = Constant('__NR_lookup_dcookie',1237)
__NR_io_setup = Constant('__NR_io_setup',1238)
__NR_io_destroy = Constant('__NR_io_destroy',1239)
__NR_io_getevents = Constant('__NR_io_getevents',1240)
__NR_io_submit = Constant('__NR_io_submit',1241)
__NR_io_cancel = Constant('__NR_io_cancel',1242)
__NR_epoll_create = Constant('__NR_epoll_create',1243)
__NR_epoll_ctl = Constant('__NR_epoll_ctl',1244)
__NR_epoll_wait = Constant('__NR_epoll_wait',1245)
__NR_restart_syscall = Constant('__NR_restart_syscall',1246)
__NR_semtimedop = Constant('__NR_semtimedop',1247)
__NR_timer_create = Constant('__NR_timer_create',1248)
__NR_timer_settime = Constant('__NR_timer_settime',1249)
__NR_timer_gettime = Constant('__NR_timer_gettime',1250)
__NR_timer_getoverrun = Constant('__NR_timer_getoverrun',1251)
__NR_timer_delete = Constant('__NR_timer_delete',1252)
__NR_clock_settime = Constant('__NR_clock_settime',1253)
__NR_clock_gettime = Constant('__NR_clock_gettime',1254)
__NR_clock_getres = Constant('__NR_clock_getres',1255)
__NR_clock_nanosleep = Constant('__NR_clock_nanosleep',1256)
__NR_fstatfs64 = Constant('__NR_fstatfs64',1257)
__NR_statfs64 = Constant('__NR_statfs64',1258)
__NR_mbind = Constant('__NR_mbind',1259)
__NR_get_mempolicy = Constant('__NR_get_mempolicy',1260)
__NR_set_mempolicy = Constant('__NR_set_mempolicy',1261)
__NR_mq_open = Constant('__NR_mq_open',1262)
__NR_mq_unlink = Constant('__NR_mq_unlink',1263)
__NR_mq_timedsend = Constant('__NR_mq_timedsend',1264)
__NR_mq_timedreceive = Constant('__NR_mq_timedreceive',1265)
__NR_mq_notify = Constant('__NR_mq_notify',1266)
__NR_mq_getsetattr = Constant('__NR_mq_getsetattr',1267)
__NR_kexec_load = Constant('__NR_kexec_load',1268)
__NR_vserver = Constant('__NR_vserver',1269)
__NR_waitid = Constant('__NR_waitid',1270)
__NR_add_key = Constant('__NR_add_key',1271)
__NR_request_key = Constant('__NR_request_key',1272)
__NR_keyctl = Constant('__NR_keyctl',1273)
__NR_ioprio_set = Constant('__NR_ioprio_set',1274)
__NR_ioprio_get = Constant('__NR_ioprio_get',1275)
__NR_set_zone_reclaim = Constant('__NR_set_zone_reclaim',1276)
__NR_inotify_init = Constant('__NR_inotify_init',1277)
__NR_inotify_add_watch = Constant('__NR_inotify_add_watch',1278)
__NR_inotify_rm_watch = Constant('__NR_inotify_rm_watch',1279)
__NR_migrate_pages = Constant('__NR_migrate_pages',1280)
__NR_openat = Constant('__NR_openat',1281)
__NR_mkdirat = Constant('__NR_mkdirat',1282)
__NR_mknodat = Constant('__NR_mknodat',1283)
__NR_fchownat = Constant('__NR_fchownat',1284)
__NR_futimesat = Constant('__NR_futimesat',1285)
__NR_newfstatat = Constant('__NR_newfstatat',1286)
__NR_unlinkat = Constant('__NR_unlinkat',1287)
__NR_renameat = Constant('__NR_renameat',1288)
__NR_linkat = Constant('__NR_linkat',1289)
__NR_symlinkat = Constant('__NR_symlinkat',1290)
__NR_readlinkat = Constant('__NR_readlinkat',1291)
__NR_fchmodat = Constant('__NR_fchmodat',1292)
__NR_faccessat = Constant('__NR_faccessat',1293)
__NR_unshare = Constant('__NR_unshare',1296)
__NR_splice = Constant('__NR_splice',1297)
__NR_set_robust_list = Constant('__NR_set_robust_list',1298)
__NR_get_robust_list = Constant('__NR_get_robust_list',1299)
__NR_sync_file_range = Constant('__NR_sync_file_range',1300)
__NR_tee = Constant('__NR_tee',1301)
__NR_vmsplice = Constant('__NR_vmsplice',1302)
__NR_fallocate = Constant('__NR_fallocate',1303)
__NR_getcpu = Constant('__NR_getcpu',1304)
__NR_epoll_pwait = Constant('__NR_epoll_pwait',1305)
__NR_utimensat = Constant('__NR_utimensat',1306)
__NR_signalfd = Constant('__NR_signalfd',1307)
__NR_timerfd = Constant('__NR_timerfd',1308)
__NR_eventfd = Constant('__NR_eventfd',1309)
__NR_timerfd_create = Constant('__NR_timerfd_create',1310)
__NR_timerfd_settime = Constant('__NR_timerfd_settime',1311)
__NR_timerfd_gettime = Constant('__NR_timerfd_gettime',1312)
__SYS_NERR = Constant('__SYS_NERR',((129) + 1))
_SYS_TIME_H = Constant('_SYS_TIME_H',1)
SYS_accept = Constant('SYS_accept',1194)
SYS_access = Constant('SYS_access',1049)
SYS_acct = Constant('SYS_acct',1064)
SYS_add_key = Constant('SYS_add_key',1271)
SYS_adjtimex = Constant('SYS_adjtimex',1131)
SYS_afs_syscall = Constant('SYS_afs_syscall',1141)
SYS_bdflush = Constant('SYS_bdflush',1138)
SYS_bind = Constant('SYS_bind',1191)
SYS_brk = Constant('SYS_brk',1060)
SYS_capget = Constant('SYS_capget',1185)
SYS_capset = Constant('SYS_capset',1186)
SYS_chdir = Constant('SYS_chdir',1034)
SYS_chmod = Constant('SYS_chmod',1038)
SYS_chown = Constant('SYS_chown',1039)
SYS_chroot = Constant('SYS_chroot',1068)
SYS_clock_getres = Constant('SYS_clock_getres',1255)
SYS_clock_gettime = Constant('SYS_clock_gettime',1254)
SYS_clock_nanosleep = Constant('SYS_clock_nanosleep',1256)
SYS_clock_settime = Constant('SYS_clock_settime',1253)
SYS_clone = Constant('SYS_clone',1128)
SYS_clone2 = Constant('SYS_clone2',1213)
SYS_close = Constant('SYS_close',1029)
SYS_connect = Constant('SYS_connect',1192)
SYS_creat = Constant('SYS_creat',1030)
SYS_create_module = Constant('SYS_create_module',1132)
SYS_delete_module = Constant('SYS_delete_module',1134)
SYS_dup = Constant('SYS_dup',1057)
SYS_dup2 = Constant('SYS_dup2',1070)
SYS_epoll_create = Constant('SYS_epoll_create',1243)
SYS_epoll_ctl = Constant('SYS_epoll_ctl',1244)
SYS_epoll_pwait = Constant('SYS_epoll_pwait',1305)
SYS_epoll_wait = Constant('SYS_epoll_wait',1245)
SYS_eventfd = Constant('SYS_eventfd',1309)
SYS_execve = Constant('SYS_execve',1033)
SYS_exit = Constant('SYS_exit',1025)
SYS_exit_group = Constant('SYS_exit_group',1236)
SYS_faccessat = Constant('SYS_faccessat',1293)
SYS_fadvise64 = Constant('SYS_fadvise64',1234)
SYS_fallocate = Constant('SYS_fallocate',1303)
SYS_fchdir = Constant('SYS_fchdir',1035)
SYS_fchmod = Constant('SYS_fchmod',1099)
SYS_fchmodat = Constant('SYS_fchmodat',1292)
SYS_fchown = Constant('SYS_fchown',1100)
SYS_fchownat = Constant('SYS_fchownat',1284)
SYS_fcntl = Constant('SYS_fcntl',1066)
SYS_fdatasync = Constant('SYS_fdatasync',1052)
SYS_fgetxattr = Constant('SYS_fgetxattr',1222)
SYS_flistxattr = Constant('SYS_flistxattr',1225)
SYS_flock = Constant('SYS_flock',1145)
SYS_fremovexattr = Constant('SYS_fremovexattr',1228)
SYS_fsetxattr = Constant('SYS_fsetxattr',1219)
SYS_fstat = Constant('SYS_fstat',1212)
SYS_fstatfs = Constant('SYS_fstatfs',1104)
SYS_fstatfs64 = Constant('SYS_fstatfs64',1257)
SYS_fsync = Constant('SYS_fsync',1051)
SYS_ftruncate = Constant('SYS_ftruncate',1098)
SYS_futex = Constant('SYS_futex',1230)
SYS_futimesat = Constant('SYS_futimesat',1285)
SYS_getcpu = Constant('SYS_getcpu',1304)
SYS_getcwd = Constant('SYS_getcwd',1184)
SYS_getdents = Constant('SYS_getdents',1144)
SYS_getdents64 = Constant('SYS_getdents64',1214)
SYS_getegid = Constant('SYS_getegid',1063)
SYS_geteuid = Constant('SYS_geteuid',1047)
SYS_getgid = Constant('SYS_getgid',1062)
SYS_getgroups = Constant('SYS_getgroups',1077)
SYS_getitimer = Constant('SYS_getitimer',1119)
SYS_get_kernel_syms = Constant('SYS_get_kernel_syms',1135)
SYS_get_mempolicy = Constant('SYS_get_mempolicy',1260)
SYS_getpeername = Constant('SYS_getpeername',1196)
SYS_getpgid = Constant('SYS_getpgid',1079)
SYS_getpid = Constant('SYS_getpid',1041)
SYS_getpmsg = Constant('SYS_getpmsg',1188)
SYS_getppid = Constant('SYS_getppid',1042)
SYS_getpriority = Constant('SYS_getpriority',1101)
SYS_getresgid = Constant('SYS_getresgid',1075)
SYS_getresuid = Constant('SYS_getresuid',1073)
SYS_getrlimit = Constant('SYS_getrlimit',1085)
SYS_get_robust_list = Constant('SYS_get_robust_list',1299)
SYS_getrusage = Constant('SYS_getrusage',1086)
SYS_getsid = Constant('SYS_getsid',1082)
SYS_getsockname = Constant('SYS_getsockname',1195)
SYS_getsockopt = Constant('SYS_getsockopt',1204)
SYS_gettid = Constant('SYS_gettid',1105)
SYS_gettimeofday = Constant('SYS_gettimeofday',1087)
SYS_getuid = Constant('SYS_getuid',1046)
SYS_getunwind = Constant('SYS_getunwind',1215)
SYS_getxattr = Constant('SYS_getxattr',1220)
SYS_init_module = Constant('SYS_init_module',1133)
SYS_inotify_add_watch = Constant('SYS_inotify_add_watch',1278)
SYS_inotify_init = Constant('SYS_inotify_init',1277)
SYS_inotify_rm_watch = Constant('SYS_inotify_rm_watch',1279)
SYS_io_cancel = Constant('SYS_io_cancel',1242)
SYS_ioctl = Constant('SYS_ioctl',1065)
SYS_io_destroy = Constant('SYS_io_destroy',1239)
SYS_io_getevents = Constant('SYS_io_getevents',1240)
SYS_ioprio_get = Constant('SYS_ioprio_get',1275)
SYS_ioprio_set = Constant('SYS_ioprio_set',1274)
SYS_io_setup = Constant('SYS_io_setup',1238)
SYS_io_submit = Constant('SYS_io_submit',1241)
SYS_kexec_load = Constant('SYS_kexec_load',1268)
SYS_keyctl = Constant('SYS_keyctl',1273)
SYS_kill = Constant('SYS_kill',1053)
SYS_lchown = Constant('SYS_lchown',1124)
SYS_lgetxattr = Constant('SYS_lgetxattr',1221)
SYS_link = Constant('SYS_link',1031)
SYS_linkat = Constant('SYS_linkat',1289)
SYS_listen = Constant('SYS_listen',1193)
SYS_listxattr = Constant('SYS_listxattr',1223)
SYS_llistxattr = Constant('SYS_llistxattr',1224)
SYS_lookup_dcookie = Constant('SYS_lookup_dcookie',1237)
SYS_lremovexattr = Constant('SYS_lremovexattr',1227)
SYS_lseek = Constant('SYS_lseek',1040)
SYS_lsetxattr = Constant('SYS_lsetxattr',1218)
SYS_lstat = Constant('SYS_lstat',1211)
SYS_madvise = Constant('SYS_madvise',1209)
SYS_mbind = Constant('SYS_mbind',1259)
SYS_migrate_pages = Constant('SYS_migrate_pages',1280)
SYS_mincore = Constant('SYS_mincore',1208)
SYS_mkdir = Constant('SYS_mkdir',1055)
SYS_mkdirat = Constant('SYS_mkdirat',1282)
SYS_mknod = Constant('SYS_mknod',1037)
SYS_mknodat = Constant('SYS_mknodat',1283)
SYS_mlock = Constant('SYS_mlock',1153)
SYS_mlockall = Constant('SYS_mlockall',1154)
SYS_mmap = Constant('SYS_mmap',1151)
SYS_mmap2 = Constant('SYS_mmap2',1172)
SYS_mount = Constant('SYS_mount',1043)
SYS_mprotect = Constant('SYS_mprotect',1155)
SYS_mq_getsetattr = Constant('SYS_mq_getsetattr',1267)
SYS_mq_notify = Constant('SYS_mq_notify',1266)
SYS_mq_open = Constant('SYS_mq_open',1262)
SYS_mq_timedreceive = Constant('SYS_mq_timedreceive',1265)
SYS_mq_timedsend = Constant('SYS_mq_timedsend',1264)
SYS_mq_unlink = Constant('SYS_mq_unlink',1263)
SYS_mremap = Constant('SYS_mremap',1156)
SYS_msgctl = Constant('SYS_msgctl',1112)
SYS_msgget = Constant('SYS_msgget',1109)
SYS_msgrcv = Constant('SYS_msgrcv',1111)
SYS_msgsnd = Constant('SYS_msgsnd',1110)
SYS_msync = Constant('SYS_msync',1157)
SYS_munlock = Constant('SYS_munlock',1158)
SYS_munlockall = Constant('SYS_munlockall',1159)
SYS_munmap = Constant('SYS_munmap',1152)
SYS_nanosleep = Constant('SYS_nanosleep',1168)
SYS_newfstatat = Constant('SYS_newfstatat',1286)
SYS_nfsservctl = Constant('SYS_nfsservctl',1169)
SYS_ni_syscall = Constant('SYS_ni_syscall',1024)
SYS_open = Constant('SYS_open',1028)
SYS_openat = Constant('SYS_openat',1281)
SYS_pciconfig_read = Constant('SYS_pciconfig_read',1173)
SYS_pciconfig_write = Constant('SYS_pciconfig_write',1174)
SYS_perfmonctl = Constant('SYS_perfmonctl',1175)
SYS_personality = Constant('SYS_personality',1140)
SYS_pipe = Constant('SYS_pipe',1058)
SYS_pivot_root = Constant('SYS_pivot_root',1207)
SYS_poll = Constant('SYS_poll',1090)
SYS_prctl = Constant('SYS_prctl',1170)
SYS_pread = Constant('SYS_pread',1148)
SYS_ptrace = Constant('SYS_ptrace',1048)
SYS_putpmsg = Constant('SYS_putpmsg',1189)
SYS_pwrite = Constant('SYS_pwrite',1149)
SYS_query_module = Constant('SYS_query_module',1136)
SYS_quotactl = Constant('SYS_quotactl',1137)
SYS_read = Constant('SYS_read',1026)
SYS_readahead = Constant('SYS_readahead',1216)
SYS_readlink = Constant('SYS_readlink',1092)
SYS_readlinkat = Constant('SYS_readlinkat',1291)
SYS_readv = Constant('SYS_readv',1146)
SYS_reboot = Constant('SYS_reboot',1096)
SYS_recv = Constant('SYS_recv',1200)
SYS_recvfrom = Constant('SYS_recvfrom',1201)
SYS_recvmsg = Constant('SYS_recvmsg',1206)
SYS_remap_file_pages = Constant('SYS_remap_file_pages',1125)
SYS_removexattr = Constant('SYS_removexattr',1226)
SYS_rename = Constant('SYS_rename',1054)
SYS_renameat = Constant('SYS_renameat',1288)
SYS_request_key = Constant('SYS_request_key',1272)
SYS_restart_syscall = Constant('SYS_restart_syscall',1246)
SYS_rmdir = Constant('SYS_rmdir',1056)
SYS_rt_sigaction = Constant('SYS_rt_sigaction',1177)
SYS_rt_sigpending = Constant('SYS_rt_sigpending',1178)
SYS_rt_sigprocmask = Constant('SYS_rt_sigprocmask',1179)
SYS_rt_sigqueueinfo = Constant('SYS_rt_sigqueueinfo',1180)
SYS_rt_sigreturn = Constant('SYS_rt_sigreturn',1181)
SYS_rt_sigsuspend = Constant('SYS_rt_sigsuspend',1182)
SYS_rt_sigtimedwait = Constant('SYS_rt_sigtimedwait',1183)
SYS_sched_getaffinity = Constant('SYS_sched_getaffinity',1232)
SYS_sched_getparam = Constant('SYS_sched_getparam',1160)
SYS_sched_get_priority_max = Constant('SYS_sched_get_priority_max',1165)
SYS_sched_get_priority_min = Constant('SYS_sched_get_priority_min',1166)
SYS_sched_getscheduler = Constant('SYS_sched_getscheduler',1162)
SYS_sched_rr_get_interval = Constant('SYS_sched_rr_get_interval',1167)
SYS_sched_setaffinity = Constant('SYS_sched_setaffinity',1231)
SYS_sched_setparam = Constant('SYS_sched_setparam',1161)
SYS_sched_setscheduler = Constant('SYS_sched_setscheduler',1163)
SYS_sched_yield = Constant('SYS_sched_yield',1164)
SYS_select = Constant('SYS_select',1089)
SYS_semctl = Constant('SYS_semctl',1108)
SYS_semget = Constant('SYS_semget',1106)
SYS_semop = Constant('SYS_semop',1107)
SYS_semtimedop = Constant('SYS_semtimedop',1247)
SYS_send = Constant('SYS_send',1198)
SYS_sendfile = Constant('SYS_sendfile',1187)
SYS_sendmsg = Constant('SYS_sendmsg',1205)
SYS_sendto = Constant('SYS_sendto',1199)
SYS_setdomainname = Constant('SYS_setdomainname',1129)
SYS_setfsgid = Constant('SYS_setfsgid',1143)
SYS_setfsuid = Constant('SYS_setfsuid',1142)
SYS_setgid = Constant('SYS_setgid',1061)
SYS_setgroups = Constant('SYS_setgroups',1078)
SYS_sethostname = Constant('SYS_sethostname',1083)
SYS_setitimer = Constant('SYS_setitimer',1118)
SYS_set_mempolicy = Constant('SYS_set_mempolicy',1261)
SYS_setpgid = Constant('SYS_setpgid',1080)
SYS_setpriority = Constant('SYS_setpriority',1102)
SYS_setregid = Constant('SYS_setregid',1072)
SYS_setresgid = Constant('SYS_setresgid',1076)
SYS_setresuid = Constant('SYS_setresuid',1074)
SYS_setreuid = Constant('SYS_setreuid',1071)
SYS_setrlimit = Constant('SYS_setrlimit',1084)
SYS_set_robust_list = Constant('SYS_set_robust_list',1298)
SYS_setsid = Constant('SYS_setsid',1081)
SYS_setsockopt = Constant('SYS_setsockopt',1203)
SYS_set_tid_address = Constant('SYS_set_tid_address',1233)
SYS_settimeofday = Constant('SYS_settimeofday',1088)
SYS_setuid = Constant('SYS_setuid',1045)
SYS_setxattr = Constant('SYS_setxattr',1217)
SYS_set_zone_reclaim = Constant('SYS_set_zone_reclaim',1276)
SYS_shmat = Constant('SYS_shmat',1114)
SYS_shmctl = Constant('SYS_shmctl',1116)
SYS_shmdt = Constant('SYS_shmdt',1115)
SYS_shmget = Constant('SYS_shmget',1113)
SYS_shutdown = Constant('SYS_shutdown',1202)
SYS_sigaltstack = Constant('SYS_sigaltstack',1176)
SYS_signalfd = Constant('SYS_signalfd',1307)
SYS_socket = Constant('SYS_socket',1190)
SYS_socketpair = Constant('SYS_socketpair',1197)
SYS_splice = Constant('SYS_splice',1297)
SYS_stat = Constant('SYS_stat',1210)
SYS_statfs = Constant('SYS_statfs',1103)
SYS_statfs64 = Constant('SYS_statfs64',1258)
SYS_swapoff = Constant('SYS_swapoff',1095)
SYS_swapon = Constant('SYS_swapon',1094)
SYS_symlink = Constant('SYS_symlink',1091)
SYS_symlinkat = Constant('SYS_symlinkat',1290)
SYS_sync = Constant('SYS_sync',1050)
SYS_sync_file_range = Constant('SYS_sync_file_range',1300)
SYS__sysctl = Constant('SYS__sysctl',1150)
SYS_sysfs = Constant('SYS_sysfs',1139)
SYS_sysinfo = Constant('SYS_sysinfo',1127)
SYS_syslog = Constant('SYS_syslog',1117)
SYS_tee = Constant('SYS_tee',1301)
SYS_tgkill = Constant('SYS_tgkill',1235)
SYS_timer_create = Constant('SYS_timer_create',1248)
SYS_timer_delete = Constant('SYS_timer_delete',1252)
SYS_timerfd = Constant('SYS_timerfd',1308)
SYS_timerfd_create = Constant('SYS_timerfd_create',1310)
SYS_timerfd_gettime = Constant('SYS_timerfd_gettime',1312)
SYS_timerfd_settime = Constant('SYS_timerfd_settime',1311)
SYS_timer_getoverrun = Constant('SYS_timer_getoverrun',1251)
SYS_timer_gettime = Constant('SYS_timer_gettime',1250)
SYS_timer_settime = Constant('SYS_timer_settime',1249)
SYS_times = Constant('SYS_times',1059)
SYS_tkill = Constant('SYS_tkill',1229)
SYS_truncate = Constant('SYS_truncate',1097)
SYS_umask = Constant('SYS_umask',1067)
SYS_umount = Constant('SYS_umount',1044)
SYS_uname = Constant('SYS_uname',1130)
SYS_unlink = Constant('SYS_unlink',1032)
SYS_unlinkat = Constant('SYS_unlinkat',1287)
SYS_unshare = Constant('SYS_unshare',1296)
SYS_uselib = Constant('SYS_uselib',1093)
SYS_ustat = Constant('SYS_ustat',1069)
SYS_utimensat = Constant('SYS_utimensat',1306)
SYS_utimes = Constant('SYS_utimes',1036)
SYS_vhangup = Constant('SYS_vhangup',1123)
SYS_vmsplice = Constant('SYS_vmsplice',1302)
SYS_vserver = Constant('SYS_vserver',1269)
SYS_wait4 = Constant('SYS_wait4',1126)
SYS_waitid = Constant('SYS_waitid',1270)
SYS_write = Constant('SYS_write',1027)
SYS_writev = Constant('SYS_writev',1147)
