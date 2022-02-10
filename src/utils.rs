pub fn exit_if_key_not_exist(key: &str) {
    if let Err(_) = std::env::var(key) {
        log::error!("The key {} does not exist in the .env file.", key);
        std::process::exit(1);
    };
}
pub fn current_version() -> String {
    return String::from("0.0.1");
}