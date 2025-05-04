#include <stddef.h>

enum { BFD_ARCH_LAST = 0x57, BFD_ARCH_OBSCURE = 0x1 };

struct display_target {
  char *filename;
  int error;
  int count;
  size_t alloc;
  struct {
    const char *name;
    unsigned char arch[BFD_ARCH_LAST - BFD_ARCH_OBSCURE - 1];
  } *info;
};

const char ref_0x231930_gnu_binutils_version[];
const char ref_0x231950_bfd_version[];

int ref_0x5FEC0_printf(const char *format, ...) {};
void ref_0x60400_free(void *ptr) {};
void ref_0xB7AB7_display_target_list(struct display_target *arg) {};
void ref_0xB7CEB_display_target_tables(const struct display_target *arg) {};

int fix_0xB7E74_display_info() {
    struct display_target arg;

    ref_0x5FEC0_printf(ref_0x231950_bfd_version, ref_0x231930_gnu_binutils_version);

    ref_0xB7AB7_display_target_list(&arg);
    if (!arg.error)
        ref_0xB7CEB_display_target_tables(&arg);
    
    // Add free to avoid memory leak
    free(arg.info);
    return arg.error;
}