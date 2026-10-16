import csv
import os

class Person:
    def __init__(self, person_id: str, name: str, age: int, gender: str):
        self._person_id = person_id
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def person_id(self) -> str:
        return self._person_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def gender(self) -> str:
        return self._gender


class Patient(Person):
    def __init__(self, patient_id: str, name: str, age: int, gender: str, diagnosis: str):
        super().__init__(patient_id, name, age, gender)
        self._diagnosis = diagnosis

    @property
    def diagnosis(self) -> str:
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, new_diagnosis: str):
        self._diagnosis = new_diagnosis

    def update_record(self, name: str = None, age: int = None, gender: str = None, diagnosis: str = None):
        if name:
            self._name = name
        if age:
            self._age = age
        if gender:
            self._gender = gender
        if diagnosis:
            self._diagnosis = diagnosis

    def get_patient_details(self) -> str:
        return (
            f"Patient ID: {self._person_id} | "
            f"Name: {self._name} | "
            f"Age: {self._age} | "
            f"Gender: {self._gender} | "
            f"Diagnosis: {self._diagnosis}"
        )


class HospitalSystem:
    def __init__(self):
        self.patients = {}

    def register_patient(self, patient_id: str, name: str, age: int, gender: str, diagnosis: str):
        if patient_id in self.patients:
            raise ValueError("Patient ID already exists.")
        self.patients[patient_id] = Patient(patient_id, name, age, gender, diagnosis)

    def search_patient(self, patient_id: str) -> Patient:
        if patient_id not in self.patients:
            raise KeyError("Patient not found.")
        return self.patients[patient_id]

    def update_patient_record(self, patient_id: str, name: str = None, age: int = None, gender: str = None, diagnosis: str = None):
        patient = self.search_patient(patient_id)
        patient.update_record(name, age, gender, diagnosis)

    def delete_patient(self, patient_id: str):
        if patient_id not in self.patients:
            raise KeyError("Patient not found.")
        del self.patients[patient_id]

    def save_records(self, filename: str = "patients.csv"):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Patient ID", "Name", "Age", "Gender", "Diagnosis"])
                for p_id, p in self.patients.items():
                    writer.writerow([p.person_id, p.name, p.age, p.gender, p.diagnosis])
            print(f"Records successfully saved to {filename}.")
        except IOError as e:
            raise IOError(f"Failed to save file: {e}")


def main():
    hospital = HospitalSystem()

    while True:
        print("\n=== Hospital Patient Record System ===")
        print("1. Register Patient")
        print("2. Search Patient")
        print("3. Update Patient Record")
        print("4. Delete Patient Record")
        print("5. Save Records to CSV")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == '1':
                p_id = input("Enter Patient ID: ").strip()
                name = input("Enter Name: ").strip()
                age = int(input("Enter Age: "))
                gender = input("Enter Gender: ").strip()
                diagnosis = input("Enter Diagnosis: ").strip()
                hospital.register_patient(p_id, name, age, gender, diagnosis)
                print(f"Success: Patient {name} registered successfully.")

            elif choice == '2':
                p_id = input("Enter Patient ID to search: ").strip()
                patient = hospital.search_patient(p_id)
                print("\n--- Patient Found ---")
                print(patient.get_patient_details())

            elif choice == '3':
                p_id = input("Enter Patient ID to update: ").strip()
                # Verify existence first
                hospital.search_patient(p_id)
                print("Leave blank to keep existing value.")
                name = input("Enter new Name: ").strip() or None
                age_input = input("Enter new Age: ").strip()
                age = int(age_input) if age_input else None
                gender = input("Enter new Gender: ").strip() or None
                diagnosis = input("Enter new Diagnosis: ").strip() or None

                hospital.update_patient_record(p_id, name, age, gender, diagnosis)
                print("Success: Patient record updated successfully.")

            elif choice == '4':
                p_id = input("Enter Patient ID to delete: ").strip()
                hospital.delete_patient(p_id)
                print("Success: Patient record deleted successfully.")

            elif choice == '5':
                filename = input("Enter filename (default 'patients.csv'): ").strip() or "patients.csv"
                hospital.save_records(filename)

            elif choice == '6':
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except ValueError as e:
            print(f"Input Error: {e}")
        except KeyError as e:
            print(f"Lookup Error: {e}")
        except IOError as e:
            print(f"File Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
