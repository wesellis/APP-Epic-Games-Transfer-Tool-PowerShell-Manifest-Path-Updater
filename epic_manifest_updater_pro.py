            self.log_message("🎉 EPIC GAMES MANIFEST UPDATE COMPLETE!", "EPIC")
            self.log_message(f"✅ Successfully updated: {results['updated']} games", "SUCCESS")
            if results['skipped'] > 0:
                self.log_message(f"⏭️ Skipped: {results['skipped']} manifests", "WARNING")
            if results['errors'] > 0:
                self.log_message(f"❌ Errors encountered: {results['errors']}", "ERROR")
                
            self.log_message("🚀 You can now start Epic Games Launcher!", "EPIC")
            self.log_message("Your games should be recognized automatically.", "SUCCESS")
            
            # Show completion dialog with Epic styling
            result_msg = f"Epic Games Manifest Update Complete!\n\n"
            result_msg += f"✅ Updated: {results['updated']} games\n"
            if results['skipped'] > 0:
                result_msg += f"⏭️ Skipped: {results['skipped']} manifests\n"
            if results['errors'] > 0:
                result_msg += f"❌ Errors: {results['errors']}\n"
            result_msg += f"\n🚀 Ready to launch Epic Games!"
            
            messagebox.showinfo("Update Complete", result_msg)
            
        except Exception as e:
            self.log_message(f"FATAL ERROR: {str(e)}", "ERROR")
            messagebox.showerror("Critical Error", f"A critical error occurred:\n{str(e)}")
            
        finally:
            self.is_processing = False
            self.main_btn.config(state="normal", text="🔍 Scan & Update Manifests")
            self.animate_progress(False)
            self.status_var.set("Update complete - Ready for Epic Games Launcher")
            
    def animate_progress(self, start):
        """Animate the progress bar with Epic colors"""
        if start:
            self.progress.delete("all")
            self.progress_animation = 0
            self.animate_progress_step()
        else:
            if hasattr(self, 'progress_after_id'):
                self.root.after_cancel(self.progress_after_id)
            self.progress.delete("all")
            
    def animate_progress_step(self):
        """Single step of progress animation"""
        if self.is_processing:
            self.progress.delete("all")
            width = self.progress.winfo_width()
            height = self.progress.winfo_height()
            
            # Create animated gradient effect
            for i in range(0, width, 10):
                color_intensity = int(128 + 127 * abs(((i + self.progress_animation) % 60) - 30) / 30)
                color = f"#{color_intensity:02x}{color_intensity//2:02x}{255:02x}"
                self.progress.create_rectangle(i, 0, i+10, height, fill=color, outline="")
            
            self.progress_animation += 5
            self.progress_after_id = self.root.after(100, self.animate_progress_step)


def main():
    """Main application entry point"""
    # Create root window (hidden initially)
    root = tk.Tk()
    root.withdraw()  # Hide main window
    
    # Show Epic Games themed splash screen
    splash = EpicSplashScreen()
    root.wait_window(splash.splash)  # Wait for splash to close
    
    # Show main window
    root.deiconify()
    app = EpicManifestUpdaterPro(root)
    
    # Start the application
    root.mainloop()


if __name__ == "__main__":
    main()
