FROM archlinux:base-devel

RUN pacman -Syu --needed --noconfirm  \
    archlinux-keyring \
    neofetch \
    neovim \
    djvulibre \
    ghostscript \
    && pacman -Scc --noconfirm
