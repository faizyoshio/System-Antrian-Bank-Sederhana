import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pyttsx3
import threading
import heapq
from datetime import datetime
from typing import List, Optional, Tuple
import time

class QueueItem:
    
    def __init__(self, queue_number: str, customer_name: str, service_type: str, priority: int):
        self.queue_number = queue_number
        self.customer_name = customer_name
        self.service_type = service_type
        self.priority = priority
        self.timestamp = datetime.now()
        self.served_at_time: Optional[datetime] = None
        self.served_at_desk: Optional[int] = None

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.timestamp < other.timestamp
    
    def __str__(self):
        return f"{self.queue_number} - {self.customer_name}"

class VoiceNotifier:
    
    def __init__(self):
        self.engine = None
        self.is_speaking = False
        self.speech_lock = threading.Lock()
        self._initialize_engine()
    
    def _initialize_engine(self):
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 140)
            self.engine.setProperty('volume', 0.9)
            
            voices = self.engine.getProperty('voices')
            if voices:
                for voice in voices:
                    if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                        self.engine.setProperty('voice', voice.id)
                        break
        except Exception as e:
            print(f"Voice system initialization failed: {e}")
            self.engine = None
    
    def announce(self, message: str):
        if not self.engine:
            print(f"🔊 Pengumuman: {message}")
            return
        
        def speak():
            with self.speech_lock:
                if self.is_speaking:
                    return
                
                try:
                    self.is_speaking = True
                    local_engine = pyttsx3.init()
                    local_engine.setProperty('rate', 140)
                    local_engine.setProperty('volume', 0.9)
                    local_engine.say(message)
                    local_engine.runAndWait()
                    local_engine.stop()
                except Exception as e:
                    print(f"Voice announcement failed: {e}")
                    print(f"🔊 Pengumuman: {message}")
                finally:
                    self.is_speaking = False
        
        thread = threading.Thread(target=speak)
        thread.daemon = True
        thread.start()

class BankQueueSystem:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Antrian Bank - Lengkap")
        self.root.configure(bg='#f0f0f0')
        
        self.queue_heap = []
        self.next_available_number_counter = 1
        self.max_queue_number = 100
        self.served_customers: List[QueueItem] = []
        self.activity_records: List[dict] = []
        
        self.meja1_current = "---"
        self.meja2_current = "---"
        self.next_number_to_serve = "---"
        
        self.voice_notifier = VoiceNotifier()
        
        self.total_served_today = 0
        self.business_served = 0
        self.personal_served = 0
        
        self.setup_ui()
        self.update_display()
        self.start_time_update()
        
        self.voice_notifier.announce("Sistem Antrian Bank telah aktif")
        self.add_activity_log("INFO", "Sistem Antrian Bank dimulai")
    
    def setup_ui(self):
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        header_frame = tk.Frame(self.root, bg='#f0f0f0')
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        self.setup_header(header_frame)

        display_container = tk.Frame(self.root, bg='#f0f0f0')
        display_container.grid(row=1, column=0, sticky="ew", padx=20, pady=0)
        self.setup_main_display(display_container)

        control_frame = tk.Frame(self.root, bg='#f0f0f0')
        control_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)
        self.setup_control_panel(control_frame)

        bottom_frame = tk.Frame(self.root, bg='#f0f0f0')
        bottom_frame.grid(row=3, column=0, sticky="nsew", padx=20, pady=20)
        self.setup_bottom_section(bottom_frame)
    
    def setup_header(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=0)
        parent.grid_rowconfigure(0, weight=1)

        title_label = tk.Label(
            parent, 
            text="🏦 SISTEM ANTRIAN BANK", 
            font=('Arial', 28, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.grid(row=0, column=0, sticky='w')
        
        self.time_label = tk.Label(
            parent,
            text="",
            font=('Arial', 16),
            bg='#f0f0f0',
            fg='#666666'
        )
        self.time_label.grid(row=0, column=1, sticky='e')
    
    def setup_main_display(self, parent):
        parent.grid_rowconfigure(0, weight=0)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=0)
        parent.grid_columnconfigure(0, weight=1)

        header_frame = tk.Frame(parent, bg='#ff8c00', height=80)
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.pack_propagate(False)

        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=1)
        header_frame.grid_columnconfigure(2, weight=1)

        tk.Label(
            header_frame, 
            text="Meja 1", 
            font=('Arial', 20, 'bold'),
            bg='#ff8c00', 
            fg='white'
        ).grid(row=0, column=0, sticky='nsew')
        
        tk.Label(
            header_frame, 
            text="Meja 2", 
            font=('Arial', 20, 'bold'),
            bg='#ff8c00', 
            fg='white'
        ).grid(row=0, column=1, sticky='nsew')
        
        tk.Label(
            header_frame, 
            text="Nomor\nSelanjutnya", 
            font=('Arial', 20, 'bold'),
            bg='#ff8c00', 
            fg='white'
        ).grid(row=0, column=2, sticky='nsew')
        
        numbers_frame = tk.Frame(parent, bg='#ffcccb', height=120)
        numbers_frame.grid(row=1, column=0, sticky="nsew")
        numbers_frame.pack_propagate(False)

        numbers_frame.grid_columnconfigure(0, weight=1)
        numbers_frame.grid_columnconfigure(1, weight=1)
        numbers_frame.grid_columnconfigure(2, weight=1)

        self.meja1_label = tk.Label(
            numbers_frame,
            text=self.meja1_current,
            font=('Arial', 48, 'bold'),
            bg='#ffcccb',
            fg='#333333'
        )
        self.meja1_label.grid(row=0, column=0, sticky='nsew')
        
        self.meja2_label = tk.Label(
            numbers_frame,
            text=self.meja2_current,
            font=('Arial', 48, 'bold'),
            bg='#ffcccb',
            fg='#333333'
        )
        self.meja2_label.grid(row=0, column=1, sticky='nsew')
        
        self.next_label = tk.Label(
            numbers_frame,
            text=self.next_number_to_serve,
            font=('Arial', 48, 'bold'),
            bg='#ffcccb',
            fg='#333333'
        )
        self.next_label.grid(row=0, column=2, sticky='nsew')
        
        info_frame = tk.Frame(parent, bg='#ff8c00', height=80)
        info_frame.grid(row=2, column=0, sticky="ew", pady=(10, 0))
        info_frame.pack_propagate(False)
        
        info_text = ("Menampilkan nomor antrian terakhir yang dilayani\n"
                    "oleh Meja 1 dan Meja 2, serta Nomor Antrian\n"
                    "berapa yang akan dipanggil selanjutnya")
        
        tk.Label(
            info_frame,
            text=info_text,
            font=('Arial', 14),
            bg='#ff8c00',
            fg='white',
            justify=tk.CENTER
        ).place(relx=0.5, rely=0.5, anchor='center')
    
    def setup_control_panel(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        left_frame = tk.Frame(parent, bg='#f0f0f0')
        left_frame.grid(row=0, column=0, sticky="nsew")

        left_frame.grid_columnconfigure(0, weight=1)

        tk.Label(
            left_frame,
            text="Menu",
            font=('Arial', 18, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        ).grid(row=0, column=0, sticky='w', pady=(0, 15), padx=5)

        buttons_data = [
            ("1. Tambah Antrian Bisnis", '#4CAF50', self.add_business_queue),
            ("2. Tambah Antrian Personal", '#2196F3', self.add_personal_queue),
            ("3. Meja 1 memanggil", '#ff8c00', lambda: self.call_next_customer(1)),
            ("4. Meja 2 memanggil", '#ff8c00', lambda: self.call_next_customer(2)),
            ("5. Lihat Statistik", '#9C27B0', self.show_statistics),
            ("6. Pengaturan Suara", '#607D8B', self.voice_settings),
            ("7. Keluar", '#f44336', self.exit_application)
        ]
        
        for i, (text, color, command) in enumerate(buttons_data):
            left_frame.grid_rowconfigure(i + 1, weight=1)
            tk.Button(
                left_frame,
                text=text,
                font=('Arial', 12),
                bg=color,
                fg='white',
                height=2,
                command=command
            ).grid(row=i + 1, column=0, sticky="ew", pady=3, padx=5)
        
        right_frame = tk.Frame(parent, bg='#f0f0f0')
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(20, 0))
        
        tk.Label(
            right_frame,
            text="Statistik Hari Ini",
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        ).pack(anchor='w', pady=(0, 10))
        
        self.stats_frame = tk.Frame(right_frame, bg='#e8e8e8', relief=tk.RAISED, bd=2)
        self.stats_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.total_served_label = tk.Label(
            self.stats_frame,
            text="Total Dilayani: 0",
            font=('Arial', 12),
            bg='#e8e8e8'
        )
        self.total_served_label.pack(pady=5)
        
        self.business_served_label = tk.Label(
            self.stats_frame,
            text="Bisnis: 0",
            font=('Arial', 12),
            bg='#e8e8e8'
        )
        self.business_served_label.pack(pady=2)
        
        self.personal_served_label = tk.Label(
            self.stats_frame,
            text="Personal: 0",
            font=('Arial', 12),
            bg='#e8e8e8'
        )
        self.personal_served_label.pack(pady=2)
        
        self.queue_length_label = tk.Label(
            self.stats_frame,
            text="Antrian Menunggu: 0",
            font=('Arial', 12),
            bg='#e8e8e8'
        )
        self.queue_length_label.pack(pady=2)
    
    def setup_bottom_section(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        queue_frame = tk.Frame(parent, bg='#f0f0f0')
        queue_frame.grid(row=0, column=0, sticky="nsew")
        queue_frame.grid_rowconfigure(1, weight=1)
        queue_frame.grid_columnconfigure(0, weight=1)

        tk.Label(
            queue_frame,
            text="📋 Daftar Antrian Saat Ini",
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        ).grid(row=0, column=0, sticky='w', pady=(0, 10), padx=5)

        list_frame = tk.Frame(queue_frame)
        list_frame.grid(row=1, column=0, sticky="nsew")
        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.queue_listbox = tk.Listbox(
            list_frame,
            font=('Arial', 11),
            yscrollcommand=scrollbar.set,
        )
        self.queue_listbox.grid(row=0, column=0, sticky="nsew")
        scrollbar.config(command=self.queue_listbox.yview)
        
        activity_frame = tk.Frame(parent, bg='#f0f0f0')
        activity_frame.grid(row=0, column=1, sticky="nsew", padx=(20, 0))
        activity_frame.grid_rowconfigure(1, weight=1)
        activity_frame.grid_columnconfigure(0, weight=1)

        tk.Label(
            activity_frame,
            text="📊 Aktivitas Terakhir",
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        ).grid(row=0, column=0, sticky='w', pady=(0, 10), padx=5)

        activity_list_frame = tk.Frame(activity_frame)
        activity_list_frame.grid(row=1, column=0, sticky="nsew")
        activity_list_frame.grid_rowconfigure(0, weight=1)
        activity_list_frame.grid_columnconfigure(0, weight=1)

        activity_scrollbar = tk.Scrollbar(activity_list_frame)
        activity_scrollbar.grid(row=0, column=1, sticky='ns')

        self.activity_listbox = tk.Listbox(
            activity_list_frame,
            font=('Arial', 10),
            yscrollcommand=activity_scrollbar.set,
            width=40,
        )
        self.activity_listbox.grid(row=0, column=0, sticky="nsew")
        activity_scrollbar.config(command=self.activity_listbox.yview)
    
    def _get_active_queue_numbers(self) -> set[str]:
        """Mengembalikan set nomor antrian lengkap (dengan prefix) yang sedang aktif (di antrian atau di meja)."""
        active_numbers = set()
        for item in self.queue_heap:
            active_numbers.add(item.queue_number)
        if self.meja1_current != "---":
            active_numbers.add(self.meja1_current)
        if self.meja2_current != "---":
            active_numbers.add(self.meja2_current)
        return active_numbers

    def _find_next_unique_queue_number(self, queue_type: str) -> Optional[str]:
        """Mencari nomor antrian unik berikutnya yang tersedia untuk jenis antrian tertentu (1-100, berulang)."""
        prefix = "B" if queue_type == "Bisnis" else "P"
        
        active_numbers = self._get_active_queue_numbers()
        
        start_counter = self.next_available_number_counter
        
        for _ in range(self.max_queue_number):
            candidate_numerical_part = f"{self.next_available_number_counter:03d}"
            full_candidate_number = f"{prefix}{candidate_numerical_part}"
            
            self.next_available_number_counter = (self.next_available_number_counter % self.max_queue_number) + 1
            
            if full_candidate_number not in active_numbers:
                return full_candidate_number
            
            if self.next_available_number_counter == start_counter:
                break
        
        return None

    def add_business_queue(self):
        self.add_customer_dialog("Bisnis")
    
    def add_personal_queue(self):
        self.add_customer_dialog("Personal")
    
    def add_customer_dialog(self, queue_type):
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Tambah Antrian {queue_type}")
        dialog.geometry("450x350")
        dialog.configure(bg='#f0f0f0')
        dialog.transient(self.root)
        dialog.grab_set()
        
        dialog.geometry("+%d+%d" % (
            self.root.winfo_rootx() + 100,
            self.root.winfo_rooty() + 100
        ))
        
        header_color = '#4CAF50' if queue_type == 'Bisnis' else '#2196F3'
        header_frame = tk.Frame(dialog, bg=header_color, height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text=f"Pendaftaran Antrian {queue_type}",
            font=('Arial', 16, 'bold'),
            bg=header_color,
            fg='white'
        ).place(relx=0.5, rely=0.5, anchor='center')
        
        form_frame = tk.Frame(dialog, bg='#f0f0f0')
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(form_frame, text="Nama Pelanggan:", font=('Arial', 12, 'bold'), bg='#f0f0f0').pack(anchor='w', pady=(0, 5))
        name_entry = tk.Entry(form_frame, font=('Arial', 12), width=35)
        name_entry.pack(fill=tk.X, pady=(0, 15))
        name_entry.focus()
        
        tk.Label(form_frame, text="Jenis Layanan:", font=('Arial', 12, 'bold'), bg='#f0f0f0').pack(anchor='w', pady=(0, 5))
        service_var = tk.StringVar()
        service_combo = ttk.Combobox(
            form_frame, 
            textvariable=service_var,
            font=('Arial', 12),
            width=33,
            state="readonly"
        )
        
        if queue_type == "Bisnis":
            services = [
                "Pembukaan Rekening Bisnis",
                "Kredit Usaha Mikro",
                "Kredit Usaha Kecil",
                "Layanan Korporat",
                "Konsultasi Bisnis",
                "Transfer Bisnis"
            ]
        else:
            services = [
                "Pembukaan Rekening Personal",
                "Setor Tunai",
                "Tarik Tunai",
                "Kartu Kredit",
                "Konsultasi Investasi",
                "Transfer Personal"
            ]
        
        service_combo['values'] = services
        service_combo.pack(fill=tk.X, pady=(0, 20))
        service_combo.current(0)
        
        button_frame = tk.Frame(form_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        def add_customer():
            name = name_entry.get().strip()
            service = service_var.get()
            
            if not name:
                messagebox.showerror("Error", "Nama pelanggan tidak boleh kosong!")
                name_entry.focus()
                return
            
            queue_number = self._find_next_unique_queue_number(queue_type)
            
            if queue_number is None:
                messagebox.showerror("Error", "Antrian penuh! Tidak ada nomor antrian yang tersedia.")
                self.add_activity_log("ERROR", "Gagal menambahkan pelanggan: Antrian penuh")
                dialog.destroy()
                return

            priority = 1 if queue_type == "Bisnis" else 2
            
            queue_item = QueueItem(queue_number, name, service, priority)
            heapq.heappush(self.queue_heap, queue_item)
            
            self.add_activity_log("ENTRY", f"Ditambahkan: {queue_number} ({queue_type}) - {name}", queue_number)
            
            self.voice_notifier.announce(f"Selamat datang. Nomor antrian Anda adalah {queue_number}")
            
            self.update_display()
            
            messagebox.showinfo("Berhasil", f"Nomor antrian {queue_number} telah ditambahkan!\n\nNama: {name}\nLayanan: {service}\nJenis: {queue_type}")
            dialog.destroy()
        
        tk.Button(
            button_frame,
            text="✅ Tambah Antrian",
            font=('Arial', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            width=15,
            height=2,
            command=add_customer
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="❌ Batal",
            font=('Arial', 12, 'bold'),
            bg='#f44336',
            fg='white',
            width=15,
            height=2,
            command=dialog.destroy
        ).pack(side=tk.LEFT)
        
        dialog.bind('<Return>', lambda e: add_customer())
    
    def call_next_customer(self, desk_number):
        if not self.queue_heap:
            messagebox.showinfo("Info", "Tidak ada antrian!")
            self.voice_notifier.announce("Tidak ada antrian")
            self.add_activity_log("INFO", "Percobaan memanggil, antrian kosong")
            return
        
        next_customer = heapq.heappop(self.queue_heap)
        
        next_customer.served_at_time = datetime.now()
        next_customer.served_at_desk = desk_number

        if desk_number == 1:
            self.meja1_current = next_customer.queue_number
        else:
            self.meja2_current = next_customer.queue_number
        
        self.served_customers.append(next_customer)
        self.total_served_today += 1
        
        if next_customer.priority == 1:
            self.business_served += 1
        else:
            self.personal_served += 1
        
        self.add_activity_log("SERVED", f"Dipanggil: {next_customer.queue_number} ke Meja {desk_number}", next_customer.queue_number)
        
        announcement = f"Nomor antrian {next_customer.queue_number}, silakan ke meja {desk_number}"
        self.voice_notifier.announce(announcement)
        
        self.update_display()
        
        messagebox.showinfo(
            f"Panggilan Meja {desk_number}",
            f"🔔 Memanggil: {next_customer.queue_number}\n"
            f"👤 Nama: {next_customer.customer_name}\n"
            f"🏢 Layanan: {next_customer.service_type}\n"
            f"🪑 Meja: {desk_number}\n"
            f"⏰ Waktu: {datetime.now().strftime('%H:%M:%S')}"
        )
    
    def show_statistics(self):
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Statistik Pelayanan")
        stats_window.geometry("500x400")
        stats_window.configure(bg='#f0f0f0')
        stats_window.transient(self.root)
        
        header_frame = tk.Frame(stats_window, bg='#9C27B0', height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="📊 Statistik Pelayanan Hari Ini",
            font=('Arial', 16, 'bold'),
            bg='#9C27B0',
            fg='white'
        ).place(relx=0.5, rely=0.5, anchor='center')
        
        content_frame = tk.Frame(stats_window, bg='#f0f0f0')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        stats_text = f"""
        📈 RINGKASAN PELAYANAN

        🎯 Total Pelanggan Dilayani: {self.total_served_today}
        🏢 Antrian Bisnis Dilayani: {self.business_served}
        👤 Antrian Personal Dilayani: {self.personal_served}
        ⏳ Antrian Menunggu: {len(self.queue_heap)}

        📋 NOMOR ANTRIAN BERIKUTNYA (Potensial)
        Nomor Numerik Selanjutnya: {self.next_available_number_counter:03d}

        🪑 STATUS MEJA
        Meja 1: {self.meja1_current}
        Meja 2: {self.meja2_current}

        ⏰ Waktu Update: {datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}
        """
        
        tk.Label(
            content_frame,
            text=stats_text,
            font=('Arial', 12),
            bg='#f0f0f0',
            justify=tk.LEFT
        ).pack(fill=tk.BOTH, expand=True)
        
        tk.Button(
            content_frame,
            text="Tutup",
            font=('Arial', 12),
            bg='#9C27B0',
            fg='white',
            width=15,
            command=stats_window.destroy
        ).pack(pady=(20, 0))
    
    def voice_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Pengaturan Suara")
        settings_window.geometry("400x300")
        settings_window.configure(bg='#f0f0f0')
        settings_window.transient(self.root)
        
        header_frame = tk.Frame(settings_window, bg='#607D8B', height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="🔊 Pengaturan Suara",
            font=('Arial', 16, 'bold'),
            bg='#607D8B',
            fg='white'
        ).place(relx=0.5, rely=0.5, anchor='center')
        
        content_frame = tk.Frame(settings_window, bg='#f0f0f0')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Button(
            content_frame,
            text="🎵 Test Suara",
            font=('Arial', 12),
            bg='#4CAF50',
            fg='white',
            width=20,
            command=lambda: self.voice_notifier.announce("Test suara sistem antrian bank")
        ).pack(pady=10)
        
        voice_status = "Aktif" if self.voice_notifier.engine else "Tidak Aktif"
        tk.Label(
            content_frame,
            text=f"Status Suara: {voice_status}",
            font=('Arial', 12),
            bg='#f0f0f0'
        ).pack(pady=5)
        
        instructions = """
        Pengaturan Suara:
        • Sistem menggunakan text-to-speech
        • Suara akan mengumumkan nomor antrian
        • Jika suara tidak berfungsi, pesan akan ditampilkan di konsol
        • Pastikan speaker/headphone terhubung
        """
        
        tk.Label(
            content_frame,
            text=instructions,
            font=('Arial', 10),
            bg='#f0f0f0',
            justify=tk.LEFT
        ).pack(pady=10, fill=tk.X)
        
        tk.Button(
            content_frame,
            text="Tutup",
            font=('Arial', 12),
            bg='#607D8B',
            fg='white',
            width=15,
            command=settings_window.destroy
        ).pack(pady=(20, 0))
    
    def exit_application(self):
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar dari sistem?"):
            self.voice_notifier.announce("Sistem antrian bank akan di tutup. Terima kasih.")
            self.add_activity_log("INFO", "Sistem Antrian Bank dimatikan")
            self.root.after(6000, self.root.quit)
    
    def add_activity_log(self, action_type: str, details: str, ticket_number: Optional[str] = None):
        timestamp = datetime.now()
        log_message = f"[{timestamp.strftime('%H:%M:%S')}] {details}"
        
        self.activity_listbox.insert(0, log_message)
        
        if self.activity_listbox.size() > 50:
            self.activity_listbox.delete(50, tk.END)
        
        self.activity_records.insert(0, {
            "timestamp": timestamp,
            "action": action_type,
            "ticket_number": ticket_number,
            "details": details
        })
    
    def update_display(self):
        self.meja1_label.config(text=self.meja1_current)
        self.meja2_label.config(text=self.meja2_current)
        
        if self.queue_heap:
            self.next_number_to_serve = self.queue_heap[0].queue_number
        else:
            self.next_number_to_serve = "---"
        self.next_label.config(text=self.next_number_to_serve)
        
        self.total_served_label.config(text=f"Total Dilayani: {self.total_served_today}")
        self.business_served_label.config(text=f"Bisnis: {self.business_served}")
        self.personal_served_label.config(text=f"Personal: {self.personal_served}")
        self.queue_length_label.config(text=f"Antrian Menunggu: {len(self.queue_heap)}")
        
        self.queue_listbox.delete(0, tk.END)
        
        sorted_queue = sorted(self.queue_heap)
        
        for i, item in enumerate(sorted_queue, 1):
            priority_text = "🏢 BISNIS" if item.priority == 1 else "👤 PERSONAL"
            display_text = f"{i:2d}. {item.queue_number} ({priority_text}) - {item.customer_name}"
            self.queue_listbox.insert(tk.END, display_text)
        
        if not sorted_queue:
            self.queue_listbox.insert(tk.END, "📭 Tidak ada antrian")
    
    def start_time_update(self):
        def update_time():
            current_time = datetime.now().strftime("⏰ %H:%M:%S - %d/%m/%Y")
            self.time_label.config(text=current_time)
            self.root.after(1000, update_time)
        
        update_time()

def main():
    root = tk.Tk()

    root.attributes('-fullscreen', True)

    app = BankQueueSystem(root)
            
    def on_closing():
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar?"):
            app.voice_notifier.announce("Sistem ditutup. Terima kasih.")
            app.add_activity_log("INFO", "Sistem Antrian Bank dimatikan")
            root.after(1500, root.destroy)
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    root.mainloop()

if __name__ == "__main__":
    print("🏦 Memulai Sistem Antrian Bank...")
    print("📋 Fitur:")
    print("   • Antrian prioritas (Bisnis > Personal)")
    print("   • Nomor antrian berurutan 001-100, lalu ulang (dengan prefix B/P)")
    print("   • Nomor antrian unik (tidak ada duplikat aktif)")
    print("   • 2 Meja pelayanan")
    print("   • Pengumuman suara (dengan nomor antrian lengkap)")
    print("   • Statistik real-time")
    print("   • Log aktivitas")
    print("\n🚀 Memulai aplikasi...")
    
    main()
