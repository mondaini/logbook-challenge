# ForeFlight Integration Checklist

This checklist tracks the mapping between the ForeFlight logbook import/export template and our Django models. It highlights what can be mapped, what is extra in our models, and what is missing for full compatibility.

---

## Aircraft Table

| CSV Field         | Model Field (Aircraft) | Status      | Notes/Mapping                                  |
|-------------------|-----------------------|-------------|------------------------------------------------|
| AircraftCode        | guid                  | [x] Mapped   | UUID, used as PK                               |
| EquipmentType     | -                     | [ ] Missing  | Not present                                    |
| TypeCode          | -                     | [ ] Missing  | Not present                                    |
| Year              | -                     | [ ] Missing  | Not present                                    |
| Make              | make                  | [x] Mapped   |                                                |
| Model             | model                 | [x] Mapped   |                                                |
| Category          | category              | [x] Mapped   | Integer, may need mapping to string            |
| Class             | aircraft_class        | [x] Mapped   | Integer, may need mapping to string            |
| GearType          | -                     | [ ] Missing  | Not present                                    |
| EngineType        | -                     | [ ] Missing  | Not present                                    |
| Complex           | complex               | [x] Mapped   | Boolean                                        |
| HighPerformance   | high_perf             | [x] Mapped   | Boolean                                        |
| Pressurized       | -                     | [ ] Missing  | Not present                                    |
| TAA               | -                     | [ ] Missing  | Not present                                    |

**Extra Model Fields (not in CSV):**
- fin, sea, tmg, efis, fnpt, run2, power, seats, active, kg5700, rating, company, cond_log, fav_list, sub_model, aerobatic, ref_search, reference, tailwheel, default_app, default_log, default_ops, device_code, aircraft_code, default_launch, record_modified, platform, user_id, _modified

---

## Flights Table

| CSV Field         | Model Field (Flight)  | Status      | Notes/Mapping                                  |
|-------------------|----------------------|-------------|------------------------------------------------|
| Date              | date_utc             | [x] Mapped   | Or date_local/date_base                        |
| AircraftCode        | aircraft (FK)        | [x] Mapped   | FK to Aircraft                                 |
| From              | dep_airfield (FK)    | [x] Mapped   | FK to Airfield                                 |
| To                | arr_airfield (FK)    | [x] Mapped   | FK to Airfield                                 |
| Route             | route                | [x] Mapped   |                                                |
| TimeOut           | dep_time_utc         | [x] Mapped   | Integer, may need formatting                   |
| TimeOff           | to_time_utc          | [x] Mapped   | Integer, may need formatting                   |
| TimeOn            | arr_time_utc         | [x] Mapped   | Integer, may need formatting                   |
| TimeIn            | ldg_time_utc         | [x] Mapped   | Integer, may need formatting                   |
| OnDuty            | -                    | [ ] Missing  | Not present                                    |
| OffDuty           | -                    | [ ] Missing  | Not present                                    |
| TotalTime         | min_total            | [x] Mapped   | Integer, may need formatting                   |
| PIC               | min_pic              | [x] Mapped   | Integer, may need formatting                   |
| SIC               | min_cop              | [x] Mapped   | Integer, may need formatting                   |
| Night             | min_night            | [x] Mapped   | Integer, may need formatting                   |
| Solo              | min_u1               | [x] Mapped   | (Assumed)                                      |
| CrossCountry      | min_xc               | [x] Mapped   | Integer, may need formatting                   |
| NVG               | -                    | [ ] Missing  | Not present                                    |
| NVGOps            | -                    | [ ] Missing  | Not present                                    |
| Distance          | -                    | [ ] Missing  | Not present                                    |
| DayTakeoffs       | to_day               | [x] Mapped   | Integer                                        |
| DayLandingsFullStop | ldg_day            | [x] Mapped   | Integer                                        |
| NightTakeoffs     | to_night             | [x] Mapped   | Integer                                        |
| NightLandingsFullStop | ldg_night         | [x] Mapped   | Integer                                        |
| AllLandings       | -                    | [ ] Missing  | Not present                                    |
| ActualInstrument  | min_ifr              | [x] Mapped   | Integer                                        |
| SimulatedInstrument | min_imt            | [x] Mapped   | Integer                                        |
| HobbsStart        | hobbs_out            | [x] Mapped   | Integer                                        |
| HobbsEnd          | hobbs_in             | [x] Mapped   | Integer                                        |
| TachStart         | -                    | [ ] Missing  | Not present                                    |
| TachEnd           | -                    | [ ] Missing  | Not present                                    |
| Holds             | holding              | [x] Mapped   | Integer                                        |
| Approach1-6       | tag_approach         | [x] Mapped   | String, may need parsing                       |
| DualGiven         | min_dual             | [x] Mapped   | Integer                                        |
| DualReceived      | min_exam             | [x] Mapped   | Integer (assumed)                              |
| SimulatedFlight   | min_sfr              | [x] Mapped   | Integer                                        |
| GroundTraining    | training             | [x] Mapped   | String                                         |
| InstructorName    | p1 (FK)              | [x] Mapped   | FK to Pilot, may need to extract name          |
| InstructorComments| report/remarks       | [x] Mapped   | Text                                           |
| Person1-6         | p1-p4, crew_list     | [x] Mapped   | FKs and string                                 |
| FlightReview      | -                    | [ ] Missing  | Not present                                    |
| Checkride         | -                    | [ ] Missing  | Not present                                    |
| IPC               | -                    | [ ] Missing  | Not present                                    |
| NVGProficiency    | -                    | [ ] Missing  | Not present                                    |
| FAA6158           | -                    | [ ] Missing  | Not present                                    |
| Custom Fields     | user_text, user_bool | [x] Mapped   | Some support                                   |

**Extra Model Fields (not in CSV):**
- pf, pax, fuel, deice, min_u2, min_u3, min_u4, arr_rwy, dep_rwy, lift_sw, to_edit, min_air, min_rel, arr_offset, dep_offset, base_offset, next_page, next_summary, arr_time_sched, dep_time_sched, flight_number, flight_search, record_modified, platform, user_id, _modified, etc.

---

## Summary

- [x] **Mapped**: Field exists in both our model and the ForeFlight template.
- [ ] **Missing**: Field exists in ForeFlight but not in our model.
- **Extra**: Field exists in our model but not in ForeFlight.

Update this checklist as models or integration logic evolves. 