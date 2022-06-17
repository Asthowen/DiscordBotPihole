pub fn exit_if_key_not_exist(key: &str) {
    if std::env::var(key).is_err() {
        log::error!("The key {} does not exist in the .env file.", key);
        std::process::exit(1);
    }
}
pub fn exit_if_keys_not_exist(keys: &[&str]) {
    for key in keys {
        exit_if_key_not_exist(key);
    }
}
pub fn current_version() -> String {
    String::from("0.0.1")
}