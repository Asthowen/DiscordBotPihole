#![allow(
    clippy::implicit_return,
    clippy::missing_inline_in_public_items,
    clippy::must_use_candidate,
    clippy::indexing_slicing,
    clippy::shadow_reuse,
    clippy::return_self_not_must_use,
    clippy::unwrap_used,
    clippy::exit,
    clippy::module_name_repetitions,
    clippy::non_ascii_literal,
    clippy::missing_const_for_fn,
    clippy::integer_arithmetic,
    clippy::integer_division,
    clippy::exhaustive_structs,
    clippy::pub_use,
    clippy::wildcard_imports,
    clippy::mod_module_files,
    clippy::separated_literal_suffix,
    clippy::else_if_without_else,
    clippy::module_inception
)]
#![deny(clippy::needless_return)]

pub mod client;
pub mod commands;
pub mod utils;
