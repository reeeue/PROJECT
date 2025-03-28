<pre> <code>
/root/source
│
├── web/                                # Web 관련 Code
│   ├── gui/                            # Web - Front-End : React JS
│   └── lib/                            # 관련 Library
│
├── chrome_extension/                   # Chrome Extension 관련 Code
│   ├── gui/                            # Chrome Extension - Front-End : Vanilla JS
│   └── lib/                            # 관련 Library
│
├── server/                             # Server - Back-End : FAST API
│   ├── app/                            # Main
│   ├── sessions/                       # User Sessions
│   └── api/                            # API
│
├── core_engine/                        # Core Engine
│   ├── fast_engine/                    # Fast Scan Engine : 관련 Plug-In 실행
│   ├── full_engine/                    # Full Scan Engine : 관련 Plug-In 실행
│   └── plugins/                        # Plug-In Modules
│       ├── url_modules/                # Phsihng Web Site의 'URL 관련 특징'을 바탕으로 Scan
│       ├── html_modules/               # Phsihng Web Site의 'HTML 관련 특징'을 바탕으로 Scan
│       ├── js_modules/                 # Phsihng Web Site의 'JS 관련 특징'을 바탕으로 Scan
│       └── others_modules/             # Phsihng Web Site의 '그 외의 특징'을 바탕으로 Scan
│
├── db/                                 # DB
│   ├── phishing_url_db/                # Phishing URL DB (Phishing Web Site URL 저장)
│   └── phishing_data_db/               # Phishing Data DB (Scan에 사용할 Data 저장)
│
├── configs/                            # 설정 파일 (env, DB, logging, plugin 등)
│
└── scripts/                            # Scripts
</code> </pre>
