#include <iostream>
#include <fstream>
#include <string>

// تابع بازگشتی برای ساخت پسووردها بر اساس الگو
void generate_with_mask(std::ofstream& file, std::string current, const std::string& mask, const std::string& chars, int index) {
    // وقتی به انتهای الگو رسیدیم، کلمه کامل شده و در فایل ذخیره می‌شود
    if (index == mask.length()) {
        file << current << "\n";
        return;
    }

    // اگر جایگاه فعلی مجهول بود ('?') تمام حروف انتخابی را تست کن
    if (mask[index] == '?') {
        for (char c : chars) {
            generate_with_mask(file, current + c, mask, chars, index + 1);
        }
    } 
    // اگر حرف ثابت بود، همان را قرار بده و برو مرحله بعدی
    else {
        generate_with_mask(file, current + mask[index], mask, chars, index + 1);
    }
}

// رابطی که پایتون آن را صدا می‌زند
extern "C" {
    void create_wordlist_mask(const char* mask_cstr, const char* charset_cstr, const char* output_filename) {
        std::ofstream file(output_filename);
        if (!file.is_open()) {
            return;
        }

        std::string mask(mask_cstr);
        std::string chars(charset_cstr);
        
        generate_with_mask(file, "", mask, chars, 0);
        
        file.close();
    }
}
