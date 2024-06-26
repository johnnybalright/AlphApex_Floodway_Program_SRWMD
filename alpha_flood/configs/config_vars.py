from .config import PARENT_DIR, BASE_DIR, TEMPLATE_DIR
from loggers.logger import setup_logger

logger = setup_logger(__name__, __name__)

#directory configs
dir_1 = "Cadd"
file_11_template = "{projectnumber}-Base-TOPO.dwg"
file_12_template = "{projectnumber}-Plan-SITE.dwg"
file_13_template = "{projectnumber}-Residence.dst"
file_14 = ""
file_15 = ""
# file_14 = "fdot_controlplans.dwg"
# file_15 = "floodvent_fs.pdf"
file_16_template = "{projectnumber}-PermitTable.xlsx"
sub_dir_11 = "map_imports"
file_111 = ""
file_112 = ""
file_113 = ""
file_114 = ""
file_115 = ""
sub_dir_12 = ""
file_121 = ""
file_122 = ""
file_123 = ""
file_124 = ""
file_125 = ""
sub_dir_111 = "hec"
sub_dir_112 = "parc"
sub_dir_113 = "surf"
sub_dir_114 = "struc"
sub_dir_115 = "pts"
sub_dir_116 = "prj"

dir_2 = "Correspondence"
file_21 = ""
file_22 = ""
file_23 = ""
file_24 = ""
file_25 = ""
sub_dir_21 = ""
file_211 = ""
file_212 = ""
file_213 = ""
file_214 = ""
file_215 = ""
sub_dir_22 = ""
file_221 = ""
file_222 = ""
file_223 = ""
file_224 = ""
file_225 = ""

dir_3 = "Deliverables"
file_31 = ""
file_32 = ""
file_33 = ""
file_34 = ""
file_35 = ""
sub_dir_31 = "District-Submittal-YYYY.MM.DD"
file_311_template = "{projectnumber}-FinalPlans-YYYY.MM.DD.pdf"
file_312_template = "{projectnumber}-ZeroRise-Certification-YYYY.MM.DD.pdf"
file_313 = ""
file_314 = ""
file_315 = ""
sub_dir_32 = "County-Submittal-YYYY.MM.DD"
file_321 = ""
file_322 = ""
file_323 = ""
file_324 = ""
file_325 = ""

dir_4 = "GIS"
file_41 = ""
file_42 = ""
file_43 = ""
file_44 = ""
file_45 = ""
sub_dir_41 = "QGIS"
file_411 = ""
file_412 = ""
file_413 = ""
file_414 = ""
file_415 = ""
sub_dir_42 = "GPX"
file_421 = ""
file_422 = ""
file_423 = ""
file_424 = ""
file_425 = ""

dir_5 = "HECRAS"
# file_51 = ""
file_52 = ""
file_53 = ""
file_54 = ""
file_55 = ""
sub_dir_51 = "Model"
file_51_template = "{projectnumber}-ModelDesign.xlsx"

file_512 = ""
file_513 = ""
file_514 = ""
file_515 = ""
sub_dir_52 = "Report"
file_521_template = "{projectnumber}-ModelDesign.xlsx"
file_522_template = "{projectnumber}-ParcelData.pdf"
file_523_template = "{projectnumber}-FloodReport.pdf"
file_524_template = "{projectnumber}-RiverMile.pdf"
file_525_template = "{projectnumber}-ModelOutputTableSummary.pdf"
file_526_template = "{projectnumber}.App-5-PrePostEXBT.pdf"
file_527_template = "{projectnumber}.App-6-HECRAS-DATA-EXISTING.pdf"
file_528_template = "{projectnumber}.App-7-HECRAS-DATA-PROPOSED.pdf"
file_529_template = "{projectnumber}-NoRise-Certification-FINAL.pdf"
file_529_1_template = "{projectnumber}-NoRise-Certificaton-Narrative.pdf"
file_529_2_template = "{projectnumber}-Report-Plan-Post.pdf"
file_529_3_template = "{projectnumber}-Report-Plan-Pre.pdf"
sub_dir_511 = "Current"
file_5111 = ""
file_5112 = ""
file_5113 = ""
file_5114 = ""
file_5115 = ""
sub_dir_512 = "Proposed"
file_5121 = ""
file_5122 = ""
file_5123 = ""
file_5124 = ""
file_5125 = ""

dir_6 = "Others"
file_61 = ""
file_62 = ""
file_63 = ""
file_64 = ""
file_65 = ""
sub_dir_61 = "Survey"
file_611 = ""
file_612 = ""
file_613 = ""
file_614 = ""
file_615 = ""
sub_dir_62 = "Structural"
file_621 = ""
file_622 = ""
file_623 = ""
file_624 = ""
file_625 = ""
sub_dir_63 = "FDOT-SRWMD Erosion Control Measures"
file_631 = ""
file_632 = ""
file_633 = ""
file_634 = ""
file_635 = ""

dir_7 = "PM"
file_71_template = "{projectnumber}-Agent-Letter.pdf"
file_72_template = "{projectnumber}-As-Built.pdf"
file_73_template = "{projectnumber}-CORPS-App.pdf"
file_74_template = "{projectnumber}-WOD-App.pdf"
file_75_template = "{projectnumber}-Project Data-Master.txt"
sub_dir_71 = ""
file_711 = ""
file_712 = ""
file_713 = ""
file_714 = ""
file_715 = ""
sub_dir_72 = ""
file_721 = ""
file_722 = ""
file_723 = ""
file_724 = ""
file_725 = ""

dir_8 = "Property"
file_81_template = "{projectnumber}-FloodReport.pdf"
file_82_template = "{projectnumber}-PropDetails.pdf"
file_83_template = "{projectnumber}-PropDrivingDirections.pdf"
file_84 = ""
file_85 = ""
sub_dir_81 = ""
file_811 = ""
file_812 = ""
file_813 = ""
file_814 = ""
file_815 = ""
sub_dir_82 = ""
file_821 = ""
file_822 = ""
file_823 = ""
file_824 = ""
file_825 = ""

dir_9 = "Permitting"
file_91 = ""
file_92 = ""
file_93 = ""
file_94 = ""
file_95 = ""
sub_dir_91 = "ExistingPermits"
file_911 = ""
file_912 = ""
file_913 = ""
file_914 = ""
file_915 = ""
sub_dir_92 = "RAI"
file_921 = ""
file_922 = ""
file_923 = ""
file_924 = ""
file_925 = ""
sub_dir_93 = "z_Approval"
file_931 = ""
file_932 = ""
file_933 = ""
file_934 = ""
file_935 = ""

dir_10 = "Plans"
file_101 = ""
file_102 = ""
file_103 = ""
file_104 = ""
file_105 = ""
sub_dir_101 = "John"
file_1011 = ""
file_1012 = ""
file_1013 = ""
file_1014 = ""
file_1015 = ""
sub_dir_102 = "Final for Review"
file_1021 = ""
file_1022 = ""
file_1023 = ""
file_1024 = ""
file_1025 = ""
sub_dir_103 = "Progress Set-YYYY.MM.DD"
file_1031 = ""
file_1032 = ""
file_1033 = ""
file_1034 = ""
file_1035 = ""

dir_11 = "zz_python_do_not_touch"

#template configs
src_1 = PARENT_DIR / "templates/master_norise.dwg"
dst_1_template = BASE_DIR / "Cadd/{projectnumber}-Base-TOPO.dwg"
src_2 = PARENT_DIR / "templates/master_norise.dwg"
dst_2_template = BASE_DIR / "Cadd/{projectnumber}-Plan-SITE.dwg"
src_3 = PARENT_DIR / "templates/sheetset.dst"
dst_3_template = BASE_DIR / "Cadd/{projectnumber}-Residence.dst"
src_4 = PARENT_DIR / "templates/fdot_controlplans.dwg"
dst_4_template = BASE_DIR / "Cadd/{projectnumber}-FDOT_Control_Plans.dwg"
src_5 = PARENT_DIR / "templates/floodvent_fs.pdf"
dst_5_template = BASE_DIR / "Cadd/Flood-Vent-FS-HEX-Submittal-3.15.pdf"
src_6 = PARENT_DIR / "templates/xxxx_permittable.xlsx"
dst_6_template = BASE_DIR / "Cadd/{projectnumber}-PermitTable.xlsx"
src_7 = TEMPLATE_DIR / "current_hecras_data/Suwannee"
dst_7_template = BASE_DIR / "HECRAS/Model/Current"
src_8 = PARENT_DIR / "templates/fdot_srwmd_ecm"
dst_8_template = BASE_DIR / "Others/FDOT_SRWMD_Erosion_Control_Measures"
src_9 = PARENT_DIR / "templates/ace_templates"
dst_9_template = BASE_DIR / "z_Templates"
# src_10 = PARENT_DIR / "templates/lastools/bin"
# dst_10_template = BASE_DIR / "GIS/QGIS/lastools"
src_11 = ""
dst_11_template = ""
src_12 = ""
dst_12_template = ""
src_13 = ""
dst_13_template = ""
src_14 = ""
dst_14_template = ""
src_15 = ""
dst_15_template = ""
